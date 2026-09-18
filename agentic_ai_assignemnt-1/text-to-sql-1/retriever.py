import sqlite3


def get_database_schema():

    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        AND name NOT LIKE 'sqlite_%'
    """)

    tables = cursor.fetchall()

    schema = {}

    for table in tables:

        table_name = table[0]

        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()

        schema[table_name] = []

        for column in columns:

            schema[table_name].append({
                "name": column[1],
                "type": column[2]
            })

    conn.close()

    return schema


def get_foreign_key_tables():

    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()

    relationships = []

    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        AND name NOT LIKE 'sqlite_%'
    """)

    tables = cursor.fetchall()

    for table in tables:

        table_name = table[0]

        cursor.execute(
            f"PRAGMA foreign_key_list({table_name})"
        )

        foreign_keys = cursor.fetchall()

        for fk in foreign_keys:

            relationships.append({
                "from_table": table_name,
                "to_table": fk[2]
            })

    conn.close()

    return relationships


def retrieve_relevant_schema(question):

    schema = get_database_schema()
    relationships = get_foreign_key_tables()

    question_words = set(
        question.lower()
        .replace("?", "")
        .replace(",", "")
        .split()
    )

    scores = {}

    for table_name, columns in schema.items():

        score = 0

        # Match table name
        table_words = set(
            table_name.lower().replace("_", " ").split()
        )

        score += len(question_words & table_words) * 3

        # Match column names
        for column in columns:

            column_name = column["name"].lower()

            column_words = set(
                column_name.replace("_", " ").split()
            )

            score += len(question_words & column_words) * 2

        scores[table_name] = score

    # Select tables with matching terms
    selected_tables = {
        table: schema[table]
        for table, score in scores.items()
        if score > 0
    }

    # Include related foreign-key tables
    changed = True

    while changed:

        changed = False

        for relationship in relationships:

            from_table = relationship["from_table"]
            to_table = relationship["to_table"]

            if from_table in selected_tables:
                if to_table not in selected_tables:

                    selected_tables[to_table] = schema[to_table]
                    changed = True

            if to_table in selected_tables:
                if from_table not in selected_tables:

                    selected_tables[from_table] = schema[from_table]
                    changed = True

    # If nothing matched, use full schema
    if not selected_tables:
        selected_tables = schema

    return selected_tables


def format_schema(schema):

    result = ""

    for table_name, columns in schema.items():

        result += f"\nTable: {table_name}\n"

        for column in columns:

            result += (
                f"- {column['name']} "
                f"({column['type']})\n"
            )

    return result