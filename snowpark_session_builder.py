# Make the Snowflake connection
from snowflake.snowpark import Session
import os

def connect() -> Session:
    connection_parameters = {
            "account": "sbhwstq-hqb95195",
            "user": "DATA_API",
            "password": ";8z58cDck2Em",
            "warehouse": "DATA_API_WH",  # optional
            "database": "HUMAN_RESOURCES",  # optional
        }
    return Session.builder.configs(connection_parameters).create()