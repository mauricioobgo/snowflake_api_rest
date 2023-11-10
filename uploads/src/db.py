# Make the Snowflake connection
from snowflake.snowpark import Session
import snowflake.connector
import os

def connect2() -> snowflake.connector.SnowflakeConnection:
    connection_parameters = {
            "account": "<account>",
            "user": "user",
            "password": "password",
            "warehouse": "warehouse",  # optional
            "database": "database",  # optional
        }
    return snowflake.connector.connect(**connection_parameters)