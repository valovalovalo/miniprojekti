from sqlalchemy import text

from config import db
from entities.reference import Reference


class ReferenceRepository:
    def __init__(self, database):
        self.db = database

    def get_references(self):
        result = self.db.session.execute(text("SELECT * FROM reference_entries"))
        references = result.mappings()

        return [Reference(reference) for reference in references]

    def get_reference_by_id(self, reference_id):
        """
        Function for searching reference data by id, from the database

        Returns:
            List that includes a Reference object
        """

        query = text(
            """
                SELECT * FROM reference_entries WHERE reference_entries.id = (:reference_id)
                """
        )
        query_result = self.db.session.execute(query, {"reference_id": reference_id})
        reference = query_result.mappings().first()

        return [Reference(reference)]

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

    def remove_reference(self, reference_id):
        sql = text(
            """
            DELETE FROM reference_entries WHERE id = :id
            """
        )

        self.db.session.execute(sql, {"id": reference_id})
        self.db.session.commit()


reference_repo = ReferenceRepository(db)
