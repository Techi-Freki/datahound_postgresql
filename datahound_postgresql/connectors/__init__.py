import psycopg2

from datahound.connectors import ConnectorBase


class PostgreSqlConnector(ConnectorBase):
    @staticmethod
    def get_connection(connection_string):
        return psycopg2.connect(
            host=connection_string.host,
            database=connection_string.database_name,
            user=connection_string.user,
            password=connection_string.password,
            port=connection_string.port
        )
