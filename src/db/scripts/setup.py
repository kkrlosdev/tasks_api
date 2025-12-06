from ..connection import connect
import click
import sys

def create_tasks_table():
    try:
        conn = connect()
    except Exception as e:
        raise Exception(f"Could not connect to database during table creation: {e}")

    if conn is not None:
        cursor = conn.cursor()

    try:
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS tasks(
                                        id PRIMARY KEY,
                                        name TEXT NOT NULL,
                                        begin_date DATETIME,
                                        end_date DATETIME,
                                        short_description VARCHAR(100),
                                        long_description TEXT,
                                        status INT
                    );
                    """)
        print("Table 'tasks' created successfully!")
    except Exception as e:
        raise Exception(f"Could not create table: {e}")
    finally:
        cursor.close()
        conn.close()

def drop_table(table_name: str):
    try:
        conn = connect()
    except Exception as e:
        raise Exception(f"Could not connect to database during DROP TABLE operation: {e}")

    if conn is not None:
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
    print("1. Create table 'tasks'\n2. Drop table 'tasks'\n3. Exit")
    try:
        opt = int(input("$ "))
    except Exception as e:
        print("Oooops...")
        sys.exit(1)

    match opt:
        case 1:
            create_tasks_table()
        case 2:
            condition = click.confirm("Are you completely sure? Do this on your OWN risk.")
            if condition: drop_table("tasks")
        case _:
            print("bye")