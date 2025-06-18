from datetime import date, datetime
from functools import lru_cache
from typing import Iterable, Iterator, List, Tuple, Dict
import json
from psycopg.rows import class_row
from psycopg.sql import Literal

import psycopg
from aws_lambda_powertools import Logger
from psycopg import Connection
from psycopg.rows import class_row
from psycopg.sql import SQL, Identifier

from secr.domain.model.processed_customer_data_item import (
    ProcessedCustomerDataItem,
)
from secr.domain.model.supplier import SupplierData
from secr.repository.aurora.credentials import CredentialsManager

from secr.repository.supplier_data_repository import ISupplierDataItemRepository

logger = Logger()


class AuroraSupplierDataItemRepository(ISupplierDataItemRepository):
    __credentials_manager: CredentialsManager
    __table_name = "supplier_data"
    __processed_tabel_name = "processed_data_item"

    def __init__(self, credentials_manager: CredentialsManager):
        self.__credentials_manager = credentials_manager

    def _get_conn(self) -> Connection:
        try:
            logger.info(
                f"Connecting to the database with info {self.__credentials_manager.get_credentials().get_conninfo()}"
            )
            return psycopg.connect(
                **self.__credentials_manager.get_credentials().get_conninfo(),
                connect_timeout=3,
            )
        except psycopg.OperationalError as e:
            logger.exception("Error connecting to the database.")
            raise e

    def get_company_all_suppliers(self, company_id: str):
        query = SQL(
            "SELECT * "
            + "FROM "
            + self.__table_name
            + " WHERE"
            + f" company_id = '{company_id}' "
            + ";"
        )

        with self._get_conn() as conn:
            with conn.cursor(row_factory=class_row(SupplierData)) as cur:
                cur.execute(query)
                suppliers = cur.fetchall()

        logger.info("Fetched suppliers.")
        return suppliers

    def get_verified_suppliers(self, supplier_name: list, company_id: str):
        if len(supplier_name) == 0:
            return ["Please select at least one supplier"]
        if len(supplier_name) == 1:
            supplier_name.append(supplier_name[0])

        supplier_name_tuple = tuple(supplier_name)
        if company_id is not None or company_id != "":

            query = (
                    "SELECT supplier_name, id, ARRAY_AGG(DISTINCT sic_code) AS sic_codes"
                    + " FROM "
                    + self.__table_name
                    + " WHERE"
                    + f" supplier_name in {supplier_name_tuple} "
                    + f" AND company_id = '{company_id}' "
                    + " GROUP BY supplier_name, id"
                    + ";"
            )
        else:
            query = (
                    "SELECT supplier_name, id, ARRAY_AGG(DISTINCT sic_code) AS sic_codes"
                    + " FROM "
                    + self.__table_name
                    + " WHERE"
                    + f" supplier_name in {supplier_name_tuple} "
                    + " GROUP BY supplier_name, id"
                    + ";"
            )

        with self._get_conn() as conn:
            with conn.cursor(row_factory=class_row(SupplierData)) as cur:
                # with conn.cursor() as cur:
                cur.execute(query)
                suppliers = cur.fetchall()
        return suppliers

    def update_supplier_data(self, supplier_id: str, update_fields: dict) -> SupplierData:
        if 'supplier_information' in update_fields:
            update_fields['supplier_information'] = json.dumps(update_fields['supplier_information'])

        set_clause = ", ".join([f"{key} = %({key})s" for key in update_fields.keys()])
        query = SQL(f"UPDATE {self.__table_name} SET {set_clause} WHERE id = %(id)s;")

        with self._get_conn() as conn:
            with conn.cursor() as cur:
                update_fields['id'] = supplier_id  # Add id to the parameters
                cur.execute(query, update_fields)
                conn.commit()

        # Fetch and return the updated supplier data
        return self.get_supplier_by_id(supplier_id)  # Assuming you have a method to fetch supplier by ID

    def get_supplier_by_id(self, supplier_id: str) -> SupplierData:
        query = SQL(
            "SELECT * FROM {0} WHERE id = %(id)s;"
        ).format(Identifier(self.__table_name))

        with self._get_conn() as conn:
            with conn.cursor(row_factory=class_row(SupplierData)) as cur:
                cur.execute(query, {"id": supplier_id})
                supplier = cur.fetchone()

        if supplier is None:
            raise ValueError(f"Supplier with id {supplier_id} not found.")

        return supplier

    def check_for_supplier_and_update_total_spend(self, supplier_spend_map: dict,
                                                  processed_items: list[ProcessedCustomerDataItem] = None) -> list[
        dict]:
        result_data = []

        supplier_names = list(key[0] for key in supplier_spend_map.keys())
        company_ids = list(key[1] for key in supplier_spend_map.keys())

        query = SQL(
            """
            SELECT id, supplier_name, company_id 
            FROM {0} 
            WHERE supplier_name = ANY(%s)
            AND company_id = ANY(%s)
            """
        ).format(Identifier(self.__table_name))

        with self._get_conn() as conn, conn.cursor() as cur:
            cur.execute(query, (supplier_names, company_ids))
            existing_suppliers = cur.fetchall()
            existing_supplier_map = {(s[1], s[2]): s[0] for s in existing_suppliers}

            if existing_supplier_map:
                values_list = []
                for name, cid in existing_supplier_map.keys():
                    values_list.append(f"({supplier_spend_map[(name, cid)]}, '{existing_supplier_map[(name, cid)]}')")

                values_string = ", ".join(values_list)
                update_query = SQL(
                    """
                    UPDATE {0} as t SET 
                        spend = c.spend
                    FROM (VALUES {1}) as c(spend, id)
                    WHERE c.id::uuid = t.id
                    RETURNING t.id, t.supplier_name, t.company_id
                    """
                ).format(Identifier(self.__table_name), SQL(values_string))

                cur.execute(update_query)
                result_data.extend([
                    {"id": row[0], "supplier_name": row[1], "company_id": row[2]}
                    for row in cur.fetchall()
                ])

            new_suppliers = [
                (name, cid, supplier_spend_map[(name, cid)])
                for name, cid in supplier_spend_map.keys()
                if (name, cid) not in existing_supplier_map
            ]

            if new_suppliers and processed_items:
                # Create a mapping of (supplier_name, company_id) to ProcessedCustomerDataItem
                # processed_items_map = {(item.supplier, item.company_id): item for item in processed_items}
                processed_items_map = {
                    (item.supplier, item.company_id): item
                    for item in processed_items
                    if item.category and item.category.upper() in ['SCOPE_3_PURCHASE']
                }

                # values_list = []
                # for name, cid, spend in new_suppliers:
                #     if (name, cid) in processed_items_map:
                #         item = processed_items_map[(name, cid)]
                #         escaped_name = name.replace("'", "''")
                #         values_list.append(
                #             f"('{escaped_name}', '{cid}', {spend}, "
                #             f"'{item.conversion_factor_identifier}', "
                #             f"{item.emission_conversion_factor_used}, "
                #             f"{item.energy_conversion_factor_used})"
                #         )
                values_list = []
                for name, cid, spend in new_suppliers:
                    if (name, cid) in processed_items_map:
                        item = processed_items_map[(name, cid)]
                        escaped_name = name.replace("'", "''")

                        # Handle NULL values by using the SQL NULL keyword
                        energy_factor = 'NULL' if item.energy_conversion_factor_used is None else item.energy_conversion_factor_used
                        emission_factor = 'NULL' if item.emission_conversion_factor_used is None else item.emission_conversion_factor_used
                        conversion_id = 'NULL' if item.conversion_factor_identifier is None else f"'{item.conversion_factor_identifier}'"

                        values_list.append(
                            f"('{escaped_name}', '{cid}', {spend}, "
                            f"{conversion_id}, "
                            f"{emission_factor}, "
                            f"{energy_factor})"
                        )

                if values_list:
                    values_string = ", ".join(values_list)
                    insert_query = SQL(
                        """
                        INSERT INTO {0} (supplier_name, company_id, spend, 
                            conversion_factor_identifier, emission_conversion_factor_used, 
                            energy_conversion_factor_used)
                        VALUES {1}
                        RETURNING id, supplier_name, company_id
                        """
                    ).format(Identifier(self.__table_name), SQL(values_string))

                    cur.execute(insert_query)
                    result_data.extend([
                        {"id": row[0], "supplier_name": row[1], "company_id": row[2]}
                        for row in cur.fetchall()
                    ])

            conn.commit()

        return result_data

    def check_supplier_exist(self, company_id, supplier_name):
        query = SQL(
            "SELECT * FROM {0} WHERE company_id = %s AND supplier_name = %s;"
        ).format(Identifier(self.__table_name))
        with self._get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (company_id, supplier_name))
                result = cur.fetchone()
                if result:
                    return True
                else:
                    return False

    def save_supplier_data(self, supplier_data: SupplierData) -> int:  # Change return type to int

        # check the supplier and company exists or not
        if self.check_supplier_exist(supplier_data.company_id, supplier_data.supplier_name):
            raise ValueError("Supplier already exists for the company")
        # Insert the supplier data
        query = SQL(
            "INSERT INTO {0} (supplier_name, company_id, supplier_email, supplier_category, impact, spend, "
            "conversion_factor_identifier, emission_conversion_factor_used, energy_conversion_factor_used, "
            "sic_code, status, date, is_published, supplier_information,updated_sic_code,updated_conversion_factor_identifier,updated_emission_conversion_factor_used,emission_source) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "
            "RETURNING id;"  # Add RETURNING clause
        ).format(Identifier(self.__table_name))

        with self._get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (
                    supplier_data.supplier_name,
                    supplier_data.company_id,
                    supplier_data.supplier_email,
                    supplier_data.supplier_category,
                    supplier_data.impact,
                    supplier_data.spend,
                    supplier_data.conversion_factor_identifier,
                    supplier_data.emission_conversion_factor_used,
                    supplier_data.energy_conversion_factor_used,
                    supplier_data.sic_code,
                    supplier_data.status,
                    supplier_data.date,
                    supplier_data.is_published,
                    json.dumps(supplier_data.supplier_information),  # Convert dict to JSON string
                    supplier_data.updated_sic_code,
                    supplier_data.updated_conversion_factor_identifier,
                    supplier_data.updated_emission_conversion_factor_used,
                    supplier_data.emission_source
                ))
                new_supplier_id = cur.fetchone()[0]  # Fetch the ID of the newly created record

        return self.get_supplier_by_id(new_supplier_id)

    def revert_spend_from_supplier(self, supplier_info: list) -> None:
        """
        Updates supplier spend in supplier_data table.
        supplier_info format: [(supplier_id, spend_amount), ...]
        """
        if not supplier_info:
            return

        # Create values string for the UPDATE query
        values_list = [f"('{sid}', {spend})" for sid, spend in supplier_info]
        values_string = ", ".join(values_list)

        query = SQL(
            """
            UPDATE {0} as t SET 
                spend = t.spend::numeric - c.spend
            FROM (VALUES {1}) as c(id, spend)
            WHERE c.id::uuid = t.id;
            """
        ).format(Identifier(self.__table_name), SQL(values_string))

        with self._get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                conn.commit()

    def get_carbon_emission_by_supplier(self, company_id: str) -> list[dict]:
        query = SQL(
            """
            SELECT 
                sd.supplier_name,
                SUM(pdi.kg_co2e_total_value) as total_emissions
            FROM {0} sd
            JOIN secr_data.processed_data_item pdi 
                ON sd.id::text = pdi.supplier_id
            WHERE sd.company_id = %s
            GROUP BY sd.supplier_name
            ORDER BY total_emissions DESC
            ;
            """
        ).format(Identifier(self.__table_name))

        with self._get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (company_id,))
                results = [
                    {
                        "supplier": row[0] if row[0] is not None else "N/A",
                        "emissions": float(row[1]) if row[1] is not None else 0.0
                    }
                    for row in cur.fetchall()
                ]

        return results

    def get_carbon_emission_by_sic_code(self, company_id: str) -> list[dict]:
        query = SQL(
            """
            SELECT 
                pdi.sic_code,
                SUM(pdi.kg_co2e_total_value) as total_emissions
            FROM secr_data.processed_data_item pdi 
            WHERE pdi.company_id = %s
            GROUP BY pdi.sic_code
            ORDER BY total_emissions DESC
            ;
            """
        ).format(Identifier(self.__table_name))

        with self._get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (company_id,))
                results = [
                    {
                        "sic_code": str(row[0]) if row[0] is not None else "N/A",
                        "emissions": float(row[1]) if row[1] is not None else 0.0
                    }
                    for row in cur.fetchall()
                ]

        return results

    def update_supplier_emissions_and_category(self, supplier_emissions_data: dict) -> None:
        """
        Updates supplier_data table with total emissions and category

        Args:
            supplier_emissions_data: Dictionary with supplier_id as key and [category, emissions] as value
        """
        if not supplier_emissions_data:
            return

        # Create values string for the UPDATE query
        values_list = []
        for supplier_id, (category, emissions) in supplier_emissions_data.items():
            values_list.append(f"('{supplier_id}', '{category}', {emissions})")

        values_string = ", ".join(values_list)

        query = SQL(
            """
            UPDATE {0} as t SET 
                supplier_category = c.category,
                emissions = c.emissions
            FROM (VALUES {1}) as c(id, category, emissions)
            WHERE c.id::uuid = t.id;
            """
        ).format(Identifier(self.__table_name), SQL(values_string))

        with self._get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                conn.commit()
        print("Updated supplier emissions and category")

    def calculate_and_update_supplier_aggregates(self, supplier_ids: List[str]) -> None:
        """
        Calculates total emissions and updates category for the given supplier IDs
        based on their associated processed data items.

        Args:
            supplier_ids: List of supplier IDs to update
        """
        if not supplier_ids:
            logger.warning("No supplier IDs provided for aggregate update.")
            return

        # --- Step 1: Calculate aggregates from processed_data_item table ---
        calculation_query = SQL("""
            SELECT
                supplier_id,
                SUM(COALESCE(kg_co2e_total_value, 0)) AS total_emissions,
                MAX(category) AS derived_category
            FROM {processed_table}
            WHERE supplier_id = ANY(%(supplier_ids)s)
              AND supplier_id IS NOT NULL
            GROUP BY supplier_id;
        """).format(
            processed_table=Identifier(self.__processed_tabel_name)
        )

        calculated_data: Dict[str, Tuple[str, float]] = {}
        try:
            with self._get_conn() as conn, conn.cursor() as cur:
                cur.execute(calculation_query, {"supplier_ids": list(set(supplier_ids))})
                results = cur.fetchall()

                for sid, emissions, category in results:
                    category_value = category or 'UNKNOWN'
                    emissions_value = float(emissions or 0.0)
                    calculated_data[sid] = (category_value, emissions_value)

            logger.info(f"Calculated aggregates for {len(calculated_data)} suppliers based on processed items.")

        except Exception as e:
            logger.exception("Error calculating supplier aggregates from processed items.")
            raise e

        # --- Step 2: Update the supplier_data table ---
        if not calculated_data:
            logger.warning("No aggregate data calculated, skipping update of supplier_data table.")
            return

        # Prepare values for bulk update using psycopg.sql.Literal for safety
        values_list = []
        for supplier_id, (category, emissions) in calculated_data.items():
            values_list.append(SQL("({id}, {cat}, {em})").format(
                id=Literal(supplier_id),
                cat=Literal(category),
                em=Literal(emissions)
            ))

        # Construct the bulk update query
        update_query = SQL("""
            UPDATE {supplier_table} AS t
            SET
                supplier_category = c.category,
                emissions = c.emissions
            FROM (VALUES {values}) AS c(id, category, emissions)
            WHERE t.id::text = c.id;
        """).format(
            supplier_table=Identifier(self.__table_name),
            values=SQL(', ').join(values_list)
        )

        try:
            with self._get_conn() as conn, conn.cursor() as cur:
                cur.execute(update_query)
                updated_count = cur.rowcount
                conn.commit()
                logger.info(f"Updated aggregates for {updated_count} suppliers in {self.__table_name}.")
                if updated_count != len(calculated_data):
                    logger.warning(
                        f"Mismatch: Calculated data for {len(calculated_data)} suppliers but updated {updated_count} rows in {self.__table_name}.")

        except Exception as e:
            logger.exception(f"Error updating supplier aggregates in {self.__table_name}.")
            raise e


@lru_cache
def get_supplier_data_item_repository() -> ISupplierDataItemRepository:
    """
    Always use this to fetch an instance of repository. It is cached.
    """
    return AuroraSupplierDataItemRepository(
        credentials_manager=CredentialsManager()
    )
