import sqlite3


def create_database():
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS departments (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        department_id INTEGER,
        salary REAL,
        FOREIGN KEY (department_id) REFERENCES departments(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        category TEXT,
        price REAL,
        stock INTEGER
    )
    """)

    cursor.execute("DELETE FROM departments")
    cursor.execute("DELETE FROM employees")
    cursor.execute("DELETE FROM products")

    departments = [
        (1, "Engineering"),
        (2, "HR"),
        (3, "Finance"),
        (4, "Marketing")
    ]

    employees = [
        (1, "Sai", 1, 75000),
        (2, "Rahul", 1, 85000),
        (3, "Anil", 2, 50000),
        (4, "Priya", 3, 65000),
        (5, "Sneha", 4, 55000),
        (6, "Arjun", 1, 90000)
    ]

    products = [
        (1, "Laptop", "Electronics", 75000, 10),
        (2, "Mouse", "Electronics", 1200, 50),
        (3, "Keyboard", "Electronics", 2500, 30),
        (4, "Chair", "Furniture", 8000, 15),
        (5, "Desk", "Furniture", 12000, 8)
    ]

    cursor.executemany(
        "INSERT INTO departments VALUES (?, ?)",
        departments
    )

    cursor.executemany(
        "INSERT INTO employees VALUES (?, ?, ?, ?)",
        employees
    )

    cursor.executemany(
        "INSERT INTO products VALUES (?, ?, ?, ?, ?)",
        products
    )

    conn.commit()
    conn.close()

    print("Database created successfully!")


if __name__ == "__main__":
    create_database()