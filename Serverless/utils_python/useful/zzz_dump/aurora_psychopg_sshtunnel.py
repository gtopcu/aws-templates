
from typing import Any, TypedDict
from collections import defaultdict

import psycopg
import psycopg.rows
from psycopg.sql import SQL, Identifier, Literal, Composed

from sshtunnel import SSHTunnelForwarder

SSH_USERNAME = "ec2-user"
DB_CONNECT_TIMEOUT_SEC = 5

class DBCredentials:
    def __init__(self, host, port, dbname, user, password, tunnel=None):
        self.host = host
        self.port = port
        self.dbname = dbname
        self.user = user
        self.password = password
        self.tunnel = tunnel

    def get_conninfo(self) -> dict[str, Any]:
        return {
            "host": self.host,
            "port": self.port,
            "dbname": self.dbname,
            "user": self.user,
            "password": self.password
        }

def get_aurora_db_connection(db_creds: DBCredentials, use_tunnel: bool) -> psycopg.Connection:
    if not db_creds:
        print("Must supply DB connection info")
        return None

    tunnel_server = None
    conn_params = db_creds.get_conninfo()

    if use_tunnel:
        if not db_creds.tunnel:
            print("Error: Tunnel endpoint not specified in credentials but USE_SSH_TUNNEL is True.")
            return None

        try:
            print(f"Establishing SSH tunnel to {db_creds.tunnel} for Aurora at {conn_params['host']}:{conn_params['port']}/{conn_params['dbname']}...")
            tunnel_server = SSHTunnelForwarder(
                ssh_host=db_creds.tunnel,
                ssh_username=SSH_USERNAME,
                ssh_pkey="~/.ssh/id_rsa",
                remote_bind_address=(conn_params["host"], int(conn_params["port"])),
                allow_agent=True
            )
            tunnel_server.start()
            print(f"SSH tunnel established on local port {tunnel_server.local_bind_port}.")

            conn_params["host"] = "localhost"
            conn_params["port"] = tunnel_server.local_bind_port
        except Exception as e:
            print(f"Error establishing SSH tunnel to {db_creds.tunnel}: {e}")
            if tunnel_server:
                tunnel_server.stop()
            return None
    else:
        print(f"Connecting to Aurora directly at {conn_params['host']}:{conn_params['port']}/{conn_params['dbname']}...")

    try:
        conn = psycopg.connect(
            **conn_params,
            connect_timeout=DB_CONNECT_TIMEOUT_SEC,
        )
        print("Aurora Connection successful.")
        return conn
    except psycopg.OperationalError as e:
        print(f"Error connecting to Aurora database: {e}")
        if use_tunnel:
            print(f"Ensure SSH access for {SSH_USERNAME}@{db_creds.tunnel} and valid key in ~/.ssh/id_rsa or ~/.ssh/config.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred during Aurora database connection: {e}")
        return None
