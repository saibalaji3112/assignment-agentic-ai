import sqlite3
import os


DATABASE_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "text-to-sql-1",
    "company.db"
)


def get_connection():
    return sqlite3.connect(DATABASE_PATH)


def list_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
    """)

    tables = [row[0] for row in cursor.fetchall()]

    conn.close()

    return tables


def describe_table(table_name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(f"PRAGMA table_info({table_name})")

    columns = cursor.fetchall()

    conn.close()

    return columns


def execute_sql(query):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(query)

    rows = cursor.fetchall()

    column_names = [description[0] for description in cursor.description]

    conn.close()

    return {
        "columns": column_names,
        "rows": rows
    }