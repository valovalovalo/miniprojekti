from sqlalchemy import text

from config import db
from entities.reference import Reference


def get_references():
    result = db.session.execute(
        text("SELECT id, entry_type, title, authors, year FROM reference_entries")
    )
    references = result.fetchall()
    return [
        Reference(reference[0], reference[1], reference[2], reference[3], reference[4])
        for reference in references
    ]


def get_reference_by_id(reference_id):
    query = text("""
                SELECT id, entry_type, title, authors, year FROM reference_entries WHERE reference_entries.id = (:reference_id)
                """)
    query_result = db.session.execute(query, {"reference_id":reference_id})
    reference = query_result.fetchone()
    print(reference)

    return [
        Reference(reference[0], reference[1], reference[2], reference[3], reference[4])
    ]


def create_reference(entry_type, title, authors, year):
    sql = text(
        """
        INSERT INTO reference_entries (entry_type, title, authors, year) 
        VALUES (:entry_type, :title, :authors, :year)
    """
    )

    db.session.execute(
        sql,
        {"entry_type": entry_type, "title": title, "authors": authors, "year": year},
    )
    db.session.commit()
