# Make the Snowflake connection
from snowflake.snowpark import Session
import snowflake.connector
import os

def connect2() -> snowflake.connector.SnowflakeConnection:
    connection_parameters = {
            "account": "sbhwstq-hqb95195",
            "user": "DATA_API",
            "password": ";8z58cDck2Em",
            "warehouse": "DATA_API_WH",  # optional
            "database": "HUMAN_RESOURCES",  # optional
        }
    return snowflake.connector.connect(**connection_parameters)