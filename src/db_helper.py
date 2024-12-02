from sqlalchemy import text

from config import app, db

TABLE_NAME = "reference_entries"


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


    print(f"Clearing contents from table {TABLE_NAME}")
    sql = text(f"DELETE FROM {TABLE_NAME}")

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

    if table_exists(TABLE_NAME):
        print(f"Table {TABLE_NAME} exists, dropping")
        sql = text(f"DROP TABLE {TABLE_NAME}")
        db.session.execute(sql)
        db.session.commit()

    print(f"Creating table {TABLE_NAME}")
    sql = text(f"""
    CREATE TABLE {TABLE_NAME} (
        id SERIAL PRIMARY KEY,
        entry_type VARCHAR(50) NOT NULL,
        title TEXT NOT NULL,
        authors TEXT NOT NULL,
        year INTEGER NOT NULL,
        publisher TEXT,
        isbn TEXT,
        editor TEXT,
        month TEXT,
        journal TEXT,
        volume INTEGER,
        number INTEGER,
        pages INTEGET,
        booktitle TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

    db.session.execute(sql)
    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        setup_db()
