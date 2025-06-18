from functools import lru_cache
from aws_lambda_powertools import Logger
from typing import Optional, List, Dict, Any

import psycopg
from psycopg import Connection
from psycopg.rows import dict_row
from psycopg.sql import SQL, Identifier, Literal

from secr.domain.model.conversion_factor import ConversionFactor, RangedConversionFactor, DefaultConversionFactor
from secr.repository.aroura_conversion_factor_repository import IAuroraConversionFactorRepository
from secr.repository.aurora.credentials import CredentialsManager

logger = Logger()

def filter_conversion_factors(conversion_factors, country_code):
    if not country_code:
        return conversion_factors

    regional_priorities = {
        "RER": ["Europe without Switzerland", "RER w/o CH+DE", "RER w/o CH", "RER w/o DE+NL+RU"],
        "RoE": ["Europe without Austria", "Europe without Switzerland and Austria"],
        "RNA": ["North America without Quebec", "IAI Area, North America"],
        "RAS": ["IAI Area, Asia, without China and GCC"],
        "RLA": ["IAI Area, South America"],
        "RAF": ["IAI Area, Africa"],
        "RME": ["IAI Area, Russia & RER w/o EU27 & EFTA"],
        "UCTE": ["UCTE without Germany"],
        "WECC": ["Western Electricity Coordinating Council"],
        "ENTSO": ["NORDEL", "WEU"],
    }

    # Exact match override — return only matching ones if found
    exact_matches = [cf for cf in conversion_factors if cf.country_code == country_code]
    if exact_matches:
        return exact_matches

    def get_priority(cf):
        if cf.country_code in regional_priorities and country_code in regional_priorities[cf.country_code]:
            return 2
        elif cf.country_code == "RoW":
            return 3
        elif cf.country_code == "GLO":
            return 4
        else:
            return 5

    return sorted(conversion_factors, key=get_priority)


class AuroraConversionFactorRepository(IAuroraConversionFactorRepository):
    """Repository for managing conversion factor operations in an Aurora database."""

    __table_name = "conversion_factors"

    def __init__(self, credentials_manager: CredentialsManager):
        """Initialize the repository with a credentials manager."""
        self.__credentials_manager = credentials_manager

    def _get_conn(self) -> Connection:
        """Establish a connection to the Aurora database."""
        try:
            logger.info(
                f"Connecting to database with info {self.__credentials_manager.get_credentials().get_conninfo()}")
            return psycopg.connect(
                **self.__credentials_manager.get_credentials().get_conninfo(),
                connect_timeout=3,
                row_factory=dict_row
            )
        except psycopg.OperationalError as e:
            logger.exception("Error connecting to the database.")
            raise e

    def create_conversion_factor(self, cf: ConversionFactor) -> None:
        fields = cf.dict().keys()
        values = [getattr(cf, f) for f in fields]

        query = SQL("INSERT INTO {} ({}) VALUES ({})").format(
            Identifier("secr_data", self.__table_name),
            SQL(', ').join(map(Identifier, fields)),
            SQL(', ').join(SQL('%s') for _ in fields)
        )

        with self._get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(query, values)


    def update_conversion_factor(self, cf_id: str, updates: Dict[str, Any]) -> None:
        set_clause = SQL(", ").join([
            SQL("{} = %s").format(Identifier(k)) for k in updates
        ])

        query = SQL("UPDATE {} SET {} WHERE id = %s").format(
            Identifier("secr_data", self.__table_name),
            set_clause
        )

        values = list(updates.values()) + [cf_id]

        with self._get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(query, values)

    def delete_conversion_factor(self, cf_id: str) -> None:
        query = SQL("DELETE FROM {} WHERE id = %s").format(
            Identifier("secr_data", self.__table_name)
        )

        with self._get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (cf_id,))

    def list_all_conversion_factors(self) -> List[ConversionFactor]:
        query = SQL("SELECT * FROM {}").format(Identifier("secr_data", self.__table_name))

        with self._get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                results = cur.fetchall()

        return [self._map_to_domain(result) for result in results]

    def find_by_id(self, conversion_factor_id: str) -> Optional[ConversionFactor]:
        query = SQL("SELECT * FROM {table} WHERE id = %s").format(table=Identifier(self.__table_name))
        params = (conversion_factor_id,)

        with self._get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(query, params)
                result = cur.fetchone()

        return self._map_to_domain(result) if result else None

    def find_by_units(self, unit: str) -> Optional[ConversionFactor]:
        query = SQL("SELECT * FROM {table} WHERE unit = %s LIMIT 1").format(table=Identifier(self.__table_name))
        params = (unit,)

        with self._get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(query, params)
                result = cur.fetchone()

        return self._map_to_domain(result) if result else None

    def find_by_criteria(self, criteria: Dict[str, Any], country_code: Optional[str]) -> Dict[
        str, List[ConversionFactor]]:
        query_parts = [SQL("SELECT * FROM {table} WHERE 1=1").format(table=Identifier("secr_data", self.__table_name))]
        params = []

        valid_fields = {
            "category", "vehicle_type", "vehicle_fuel_type", "vehicle_size", "fuel_type",
            "chemical_group", "regulatory_category", "transport_type",
            "waste_activity_type", "waste_type", "disposal_type", "sic_code",
            "country_code", "train_type", "water_travel_type", "flight_haul",
            "flight_class",
            "material_name", "cargo_type", "load_level", "ship_size",
            "source", "type", "reference_product"
        }

        for key, value in criteria.items():
            if key in valid_fields:
                query_parts.append(SQL(f"AND {key} like %s"))
                params.append(value)

        query = SQL(" ").join(query_parts)

        with self._get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(query, params)
                results = cur.fetchall()

        conversion_factors = [self._map_to_domain(result) for result in results if result]

        if country_code:
            conversion_factors = filter_conversion_factors(conversion_factors, country_code)

        return {
            "ranged": [cf for cf in conversion_factors if isinstance(cf, RangedConversionFactor)],
            "default": [cf for cf in conversion_factors if isinstance(cf, DefaultConversionFactor)]
        }

    def find_by_fuzzy_criteria(self, search_term: str, country_code: Optional[str] = None,
                               similarity_threshold: float = 0.3) -> List[ConversionFactor]:
        fuzzy_fields = [
            "category", "scope", "vehicle_type", "vehicle_fuel_type", "chemical_group",
            "regulatory_category", "transport_type", "vehicle_size", "fuel_type",
            "waste_activity_type", "waste_type", "disposal_type", "sic_code", "country_code",
            "train_type", "water_travel_type", "flight_haul", "flight_class",
            "unit", "cargo_type", "load_level", "ship_size", "source", "type",
            "identifier", "material_name", "synonyms", "state_code", "cas_number", "reference_product"
            "commodity_code"
        ]

        table_name = Identifier("secr_data", self.__table_name)
        search_term_literal = Literal(search_term)
        similarity_threshold_literal = Literal(similarity_threshold)

        # Base query with table name
        base_query = SQL("SELECT * FROM {} WHERE ").format(table_name)

        # Fuzzy matching conditions for each field, made case-insensitive
        fuzzy_conditions = SQL(" OR ").join(
            SQL("lower({field}::text) % lower({search_term}::text)").format(
                field=Identifier(field),
                search_term=search_term_literal
            ) for field in fuzzy_fields
        )

        # Concatenate lowercased fields for similarity condition
        concat_lower = SQL("concat({})").format(
            SQL(", ").join(SQL("lower({field}::text)").format(field=Identifier(field)) for field in fuzzy_fields)
        )
        similarity_condition = SQL(" AND similarity({concat_lower}, lower({search_term}::text)) >= {threshold}").format(
            concat_lower=concat_lower,
            search_term=search_term_literal,
            threshold=similarity_threshold_literal
        )

        # Order by similarity of material_name to search_term, case-insensitive
        order_by = SQL(" ORDER BY similarity(lower(material_name), lower({search_term}::text)) DESC").format(
            search_term=search_term_literal
        )

        # Combine all parts into a single query
        query = SQL(" ").join([base_query, fuzzy_conditions, similarity_condition, order_by])

        with self._get_conn() as conn:
            with conn.cursor() as cur:
                try:
                    logged_query = query.as_string(conn)
                    print(f"Executing query: {logged_query}")
                    cur.execute(query)
                    results = cur.fetchall()
                except psycopg.Error as e:
                    logger.exception(f"Database query failed: {e}")
                    raise

        conversion_factors = [self._map_to_domain(result) for result in results if result]

        if country_code:
            conversion_factors = filter_conversion_factors(conversion_factors, country_code)

        return conversion_factors

    def _map_to_domain(self, db_record: Dict[str, Any]) -> ConversionFactor:
        if not db_record:
            return None

        kwargs = {
            "id": db_record.get("id"),
            "category": db_record.get("category"),
            "scope": db_record.get("scope"),
            "vehicle_type": db_record.get("vehicle_type"),
            "vehicle_fuel_type": db_record.get("vehicle_fuel_type"),
            "vehicle_size": db_record.get("vehicle_size"),
            "fuel_type": db_record.get("fuel_type"),
            "chemical_group": db_record.get("chemical_group"),
            "regulatory_category": db_record.get("regulatory_category"),
            "transport_type": db_record.get("transport_type"),
            "waste_activity_type": db_record.get("waste_activity_type"),
            "waste_type": db_record.get("waste_type"),
            "disposal_type": db_record.get("disposal_type"),
            "sic_code": db_record.get("sic_code"),
            "country_code": db_record.get("country_code"),
            "train_type": db_record.get("train_type"),
            "water_travel_type": db_record.get("water_travel_type"),
            "flight_haul": db_record.get("flight_haul"),
            "flight_class": db_record.get("flight_class"),
            "total_kg_co2e_per_unit": db_record.get("total_kg_co2e_per_unit"),
            "kg_co2e_co2_per_unit": db_record.get("kg_co2e_co2_per_unit"),
            "kg_co2e_ch4_per_unit": db_record.get("kg_co2e_ch4_per_unit"),
            "kg_co2e_n2o_per_unit": db_record.get("kg_co2e_n2o_per_unit"),
            "kg_co2e_wtt_per_unit": db_record.get("kg_co2e_wtt_per_unit"),
            "kwh_energy_per_unit": db_record.get("kwh_energy_per_unit"),
            "unit": db_record.get("unit"),
            "kgco2e_per_unit": db_record.get("kgco2e_per_unit"),
            "cargo_type": db_record.get("cargo_type"),
            "load_level": db_record.get("load_level"),
            "ship_size": db_record.get("ship_size"),
            "source": db_record.get("source"),
            "type": db_record.get("type"),
            "material_name": db_record.get("material_name"),
            "start_date": db_record.get("start_date"),
            "end_date": db_record.get("end_date"),
            "identifier": db_record.get("identifier"),
            "synonyms": db_record.get("synonyms"),
            "state_code": db_record.get("state_code"),
            "cas_number": db_record.get("cas_number"),
            "reference_product": db_record.get("reference_product"),
            "commodity_code": db_record.get("commodity_code"),
            "source_agency": db_record.get("source_agency"),
        }

        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        return ConversionFactor.parse_subclass(**kwargs)


@lru_cache
def get_aurora_conversion_factor_repository() -> IAuroraConversionFactorRepository:
    return AuroraConversionFactorRepository(credentials_manager=CredentialsManager())
