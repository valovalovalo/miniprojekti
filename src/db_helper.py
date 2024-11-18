from sqlalchemy import text

from config import app, db

table_name = "reference_entries"


def table_exists(name):

    """
    
    A function to check if a database table already exists

    ---

    Parameters

    ---
    
    name: str
        The name of the table to check

    ---

    Returns

    ---

    bool: 
        True if table exists, False if not

    """

    sql_table_existence = text(
        "SELECT EXISTS ("
        "  SELECT 1"
        "  FROM information_schema.tables"
        f" WHERE table_name = '{name}'"
        ")"
    )

    print(f"Checking if table {name} exists")
    print(sql_table_existence)

    result = db.session.execute(sql_table_existence)
    return result.fetchall()[0][0]


def reset_db():

    """
    
    Clears every row from referenced table

    """

    print(f"Clearing contents from table {table_name}")
    sql = text(f"DELETE FROM {table_name}")
    db.session.execute(sql)
    db.session.commit()


def setup_db():

    """
    
    Ensures that the database table is properly set up. If the table already exists,
    the table will be dropped and recreated with the specific schema.
    
    ---

    Calls table_exists() to check if the referenced table exists.
    If so -> the table will be dropped, recreated and commited.

    ---

    The new table will be created with following schema:
        id:         SERIAL PRIMARY KEY,
        entry_type: VARCHAR(50) NOT NULL,
        title:      TEXT NOT NULL,
        authors:    TEXT NOT NULL,
        year:       INTEGER NOT NULL,
        created_at: TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    """

    if table_exists(table_name):
        print(f"Table {table_name} exists, dropping")
        sql = text(f"DROP TABLE {table_name}")
        db.session.execute(sql)
        db.session.commit()

    print(f"Creating table {table_name}")
    sql = text(f"""
    CREATE TABLE {table_name} (
        id SERIAL PRIMARY KEY,
        entry_type VARCHAR(50) NOT NULL,
        title TEXT NOT NULL,
        authors TEXT NOT NULL,
        year INTEGER NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

    db.session.execute(sql)
    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        setup_db()
