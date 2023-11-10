# Make the Snowflake connection
from snowflake.snowpark import Session
import snowflake.connector
import os

def connect2() -> snowflake.connector.SnowflakeConnection:
    connection_parameters = {
            "account": os.environ['ACCOUNT'],
            "user": os.environ['USER'],
            "password": os.environ['PASSWORD'],
            "warehouse": os.environ['WAREHOUSE'],  # optional
            "database": os.environ['DATABASE'],  # optional
        }
    return snowflake.connector.connect(**connection_parameters)