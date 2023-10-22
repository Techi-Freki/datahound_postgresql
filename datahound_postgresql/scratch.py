from datahound import ConnectionString, DataProviderBase


connection = ConnectionString(
    'datahound_postgresql',
    host='localhost',
    database_name='cms_test',
    user='cms_user',
    password='cms_pass',
    port=5432
)


class PostgreSqlProvider(DataProviderBase):
    def __init__(self):
        super().__init__(connection)


class DataProvider(object):
    postgresql = PostgreSqlProvider()



sql = 'select * from cms_test.test_data'
records = DataProvider.postgresql.fetchall(sql)

for record in records:
    print(record)
