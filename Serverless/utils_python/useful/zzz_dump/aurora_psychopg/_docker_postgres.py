import time
import uuid
import docker
import psycopg
from contextlib import AbstractContextManager
from typing import Self


class DockerAuroraMock(AbstractContextManager):
    mock_credentials = {
        "user": "postgres",
        "password": "postgres",
        "host": "localhost",
        "port": 3822,
        "dbname": "postgres",
    }

    def __enter__(self) -> Self:
        self.__container = self._create_postgres_container()
        return self

    def __exit__(self, __exc_type, __exc_value, __traceback) -> bool | None:
        print("-------stopping DB--------")
        self.__container.stop()
        return None

    def _create_postgres_container(self):
        client = docker.from_env()
        print("Creating docker database...")
        container = client.containers.run(
            image="public.ecr.aws/docker/library/postgres:16.1",
            auto_remove=True,
            environment=dict(
                POSTGRES_USER=self.mock_credentials["user"],
                POSTGRES_PASSWORD=self.mock_credentials["password"],
            ),
            name=f"pytest-{str(uuid.uuid4())}",
            ports={"5432/tcp": self.mock_credentials["port"]},
            detach=True,
            remove=True,
        )

        # Wait for the container to start
        timeout = 20
        while timeout > 0:
            # Wait for the container to start
            try:
                with psycopg.connect(**self.mock_credentials) as db_connection:
                    print("Migrate DB .................")
                    self._create_default_tables(db_connection)
                    print("End of migration!!!")
                    break
            except psycopg.OperationalError:
                time.sleep(1)
                timeout -= 1
            except Exception as e:
                print(e)
                raise e

        return container

    def _create_default_tables(self, default_db_connection):
        with default_db_connection.cursor() as cur:
            cur.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')
            cur.execute("CREATE SCHEMA IF NOT EXISTS secr_data")
            cur.execute(
                """
        CREATE TABLE IF NOT EXISTS secr_data.processed_data_item
        (
            id SERIAL PRIMARY KEY,
            company_id text NOT NULL,
            source_id text NOT NULL,
            line_item_number integer NOT NULL,
            source_type text,
            associated_facility text,
            supplier text,
            category text,
            fuel_type text,
            vehicle_type text,
            vehicle_fuel_type text,
            regulatory_category text,
            transport_type text,

            unit_conversion_factor_used numeric,

            original_spend_value numeric,
            original_spend_unit text,
            converted_spend_value numeric,
            converted_spend_unit text,
            original_activity_value numeric,
            original_activity_unit text,
            converted_activity_value numeric,
            converted_activity_unit text,
            quantity numeric,
            scope integer,
            conversion_factor_identifier text,
            emission_conversion_factor_used numeric,
            kg_co2e_total_value numeric,
            energy_conversion_factor_used numeric,
            kwh_value numeric,
            wtt_conversion_factor_used numeric,
            kg_co2e_wtt_value numeric,
            kg_co2e_co2_value numeric,
            kg_co2e_ch4_value numeric,
            kg_co2e_n2o_value numeric,
            start_date date,
            end_date date,
            status text,
            sic_code text,
            sub_category text,
            kgco2e_per_unit numeric,
            waste_activity_type text,
            waste_type text,
            disposal_type text,
            spend_name text,
            spend_description text,
            country_code text,
            supplier_id text,
            custom_emission_factor numeric,
            custom_measurement numeric,
            custom_measurement_unit text,
            material_name text,
            chemical_group text,
            reference_product text,
            cas_number text,
            UNIQUE (company_id, source_id, line_item_number)
        )
                    """
            )
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS secr_data.supplier_data (
                company_id text NOT NULL,
                supplier_name text NOT NULL,
                supplier_email text,
                supplier_category text,
                impact text,
                spend text,
                conversion_factor_identifier text,
                emission_conversion_factor_used text,
                energy_conversion_factor_used text,
                sic_code text,
                status text,
                date date,
                is_published boolean,
                supplier_information jsonb,
                emission_source text,
                updated_sic_code text,
                updated_conversion_factor_identifier text,
                updated_emission_conversion_factor_used text,
                total_emission numeric,
                id uuid NOT NULL DEFAULT uuid_generate_v4()


            )
            """
            )

            cur.execute(
                """
               CREATE TABLE secr_data.data_request (
                id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                supplier_id VARCHAR(300) NOT NULL,
                date DATE NOT NULL,
                status VARCHAR(100),
                questionnaire_id VARCHAR(300),
                financial_year_id VARCHAR(300),
                answers jsonb

            )

            """
            )

            cur.execute(
                """
                create table secr_data.conversion_factors
                (
                    id                     serial
                        primary key,
                    category               text           not null,
                    scope                  integer        not null,
                    vehicle_type           text,
                    vehicle_fuel_type      text,
                    chemical_group         text,
                    regulatory_category    text,
                    transport_type         text,
                    vehicle_size           text,
                    fuel_type              text,
                    waste_activity_type    text,
                    waste_type             text,
                    disposal_type          text,
                    sic_code               text,
                    country_code           text,
                    train_type             text,
                    water_travel_type      text,
                    flight_haul            text,
                    flight_class           text,
                    total_kg_co2e_per_unit numeric(20, 5) not null,
                    kg_co2e_co2_per_unit   numeric(20, 5),
                    kg_co2e_ch4_per_unit   numeric(20, 5),
                    kg_co2e_n2o_per_unit   numeric(20, 5),
                    kg_co2e_wtt_per_unit   numeric(20, 5),
                    kwh_energy_per_unit    numeric(20, 5),
                    unit                   text           not null,
                    kgco2e_per_unit        numeric(15, 5),
                    cargo_type             text,
                    load_level             text,
                    ship_size              text,
                    source                 text,
                    type                   text,
                    start_date             date,
                    end_date               date,
                    identifier             text
                        unique,
                    material_name          text,
                    synonyms               text[],
                    state_code             text,
                    cas_number             text,
                    reference_product      text,
                    constraint unique_conversion_factor
                        unique (material_name, country_code, state_code, start_date, unit),
                    constraint unique_material_per_country_state_time
                        unique (material_name, country_code, state_code, start_date, cas_number, reference_product)
                )
            """
            )
