from sqlalchemy import text

from config import db
from entities.reference import Reference


class ReferenceRepository:
    def __init__(self, database):
        self.db = database

    def get_references(self):
        result = self.db.session.execute(
            text("SELECT id, entry_type, title, authors, year FROM reference_entries")
        )
        references = result.fetchall()
        return [
            Reference(
                reference[0], reference[1], reference[2], reference[3], reference[4]
            )
            for reference in references
        ]

    def create_reference(self, entry_type, title, authors, year):
        sql = text(
            """
            INSERT INTO reference_entries (entry_type, title, authors, year) 
            VALUES (:entry_type, :title, :authors, :year)
        """
        )

        self.db.session.execute(
            sql,
            {
                "entry_type": entry_type,
                "title": title,
                "authors": authors,
                "year": year,
            },
        )
        self.db.session.commit()


reference_repo = ReferenceRepository(db)
