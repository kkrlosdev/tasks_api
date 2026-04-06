import sys
import click

from db.connection import connect

def create_database_schema():
    try:
        conn = connect()
    except Exception as e:
        raise Exception(f"Could not connect to database during table creation: {e}")

    cursor = conn.cursor()

    try:
        # Activar constraints de foreign keys ya que SQLite no las valida
        # por defecto para ninguna operación.
        cursor.execute("PRAGMA foreign_keys = ON;")

        cursor.execute("""
                CREATE TABLE IF NOT EXISTS criticities(
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL UNIQUE
                );
                """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tags(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL UNIQUE
            );
            """)

        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS tasks(
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        begin_date DATETIME,
                        end_date DATETIME,
                        short_description VARCHAR(100),
                        long_description TEXT,
                        status INT,
                        criticity_id INTEGER,
                        FOREIGN KEY (criticity_id) REFERENCES criticities(id)
                        );
                    """)

        cursor.execute("""
                CREATE TABLE IF NOT EXISTS task_tags(
                    task_id INTEGER,
                    tag_id INTEGER,
                    PRIMARY KEY (task_id, tag_id),
                    FOREIGN KEY (task_id) REFERENCES tasks(id) ON DELETE CASCADE,
                    FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE CASCADE
                );
                """)

        print("Database schema created successfully!")
    except Exception as e:
        raise Exception(f"Could not create database: {e}")
    finally:
        cursor.close()
        conn.close()

def drop_table(table_name: str):
    try:
        conn = connect()
    except Exception as e:
        raise Exception(f"Could not connect to database during DROP TABLE operation: {e}")

    cursor = conn.cursor()

    try:
        cursor.execute(f"DROP TABLE {table_name};")
        print(f"Table {table_name} dropped successfully.")
    except Exception as e:
        raise Exception(f"Could not drop table '{table_name}': {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    print("1. Create database schema\n2. Drop all database\n3. Exit")
    try:
        opt = int(input("$ "))
    except Exception as e:
        print("Oooops...")
        sys.exit(1)

    match opt:
        case 1:
            create_database_schema()
        case 2:
            condition = click.confirm("Are you completely sure? Do this on your OWN risk.")
            if condition:
                drop_table("criticities")
                drop_table("tags")
                drop_table("tasks")
                drop_table("task_tags")
        case _:
            print("bye")