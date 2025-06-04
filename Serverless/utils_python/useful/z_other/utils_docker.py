
# pip install docker psychopg

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
        "port": 5422,
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
            image="public.ecr.aws/docker/library/postgres:17.1",
            auto_remove=True,
            environment=dict(
                POSTGRES_USER=self.mock_credentials["user"],
                POSTGRES_PASSWORD=self.mock_credentials["password"],
            ),
            name=f"pytondocker-{str(uuid.uuid4())}",
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
            cur.execute("CREATE SCHEMA IF NOT EXISTS my_schema")
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS my_schema.my_table
                (
                    id SERIAL PRIMARY KEY,
                    uuid NOT NULL DEFAULT uuid_generate_v4(),
                    company_id text NOT NULL,
                    line_number integer NOT NULL,
                    unit numeric(20, 5),
                    start_date date,
                    end_date date,
                    address VARCHAR(300),
                    offices text[],
                    config jsonb,
                    UNIQUE (company_id, line_item_number),
                    constraint unique_unit
                        unique (unit, start_date, end_date)
                )
                    """
            )
