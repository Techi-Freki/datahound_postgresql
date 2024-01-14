# Datahound PostgreSQL

A PostgreSQL connector for [datahound](https://github.com/Techi-Freki/datahound).

## Usage

### Extending provider base

    from datahound import DataProviderBase, ConnectionString


    # add your connection string data to the ConnectionString object
    postgres_connection = ConnectionString('datahound_postgresql',
                                          user='test_user',
                                          password='test_pass',
                                          host='localhost',
                                          port=5432
                                          database_name='test_db'
                                          )

    sqlite_connection = ConnectionString(database_path='/path/to/db.sqlite') # datahound defaults to sqlite3 when a connector_name is not passed

    # extend the DataProviderBase class
    class PostgreSqlProvider(DataProviderBase):
        def __init__(self):
            super().__init__(postgres_connection)


    class SqLiteProvider(DataProviderClass):
        def __init__(self):
            super().__init__(sqlite_connection)


    class DataProvider(object):
        postgres = PostgreSqlProvider()
        sqlite = SqLiteProvider()


    # you are now ready to use the DataProvider class to access your databases
    # see the datahound README for additional information on running queries, etc

## Changelog

1.0.0

* Initial Release.
