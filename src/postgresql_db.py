import psycopg
from psycopg import Connection, Cursor
from psycopg.rows import dict_row
from contextlib import contextmanager
import os
from dotenv import load_dotenv

load_dotenv(override=True)

DB_PARAMS = {
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT")),
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD")
}

@contextmanager
def get_connection():
    with psycopg.connect(**DB_PARAMS, row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            yield conn, cur

#to re-use the connection for each route
# def get_db():
#     with get_connection() as (conn, cur):
#         yield conn, cur


#### test the db connection ###

# def test_db_connection():
#     try:
#         with get_connection() as (conn, cur):
#             cur.execute("SELECT version();")
#             result = cur.fetchone()
#             print("Connection successful. PostgreSQL version:")
#             print(result["version"])  # Correct key when using dict_row
#     except Exception as e:
#         print("Connection failed:")
#         print(e)
#         print(DB_PARAMS)


# if __name__ == "__main__":
#     test_db_connection()