from sqlalchemy import text

from config import app, db

TABLE_NAME = "reference_entries"


def table_exists(name):
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

    print(f"Clearing contents from table {TABLE_NAME}")
    sql = text(f"DELETE FROM {TABLE_NAME}")

    db.session.execute(sql)
    db.session.commit()


def setup_db():

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
        year TEXT NOT NULL,
        publisher TEXT,
        isbn TEXT,
        editor TEXT,
        month TEXT,
        journal TEXT,
        volume TEXT,
        number TEXT,
        pages TEXT,
        booktitle TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

    db.session.execute(sql)
    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        setup_db()
