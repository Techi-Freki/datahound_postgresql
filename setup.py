from setuptools import setup

setup(
    name='datahound-postgresql',
    version='1.0.0',
    packages=['datahound_postgresql', 'datahound_postgresql.connectors'],
    url='https://python.dbcombs.com/simple/datahound_postgresql',
    license='MIT',
    author='D. Bryan Combs',
    author_email='dbcombs@gmail.com',
    description='A PostgreSQL connector for datahound',
    install_requires=['datahound', 'psycopg2'],
    extra_depency_urls=['https://python.dbcombs.com/simple'],
    entry_points={
        'datahound.connectors': ['datahound_postgresql=datahound_postgresql.connectors:PostgreSqlConnector']
    }
)
