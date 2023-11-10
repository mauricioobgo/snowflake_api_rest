from datetime import datetime
import os
import psycopg2

def formatDate(data: datetime):
    return data.strftime('%Y-%m-%dT%H:%M:%S')

def pysqlConnection():
    env_db_db = os.environ.get("DB_NAME")
    env_db_user = os.environ.get("DB_USER")
    env_db_pass = os.environ.get("DB_PASSWORD")
    env_db_host = os.environ.get("DB_HOST")
    env_db_port = os.environ.get("DB_PORT")
    if env_db_db is None:
        env_db_db = "postgres"
        env_db_user = "postgres"
        env_db_pass = "mysecretpassword"
        env_db_host = "localhost"
        env_db_port = 5432
    try:
        connection = psycopg2.connect(database=env_db_db, user=env_db_user, password=env_db_pass, host=env_db_host, port= env_db_port)
    except:
        connection = None
        pass
    return connection