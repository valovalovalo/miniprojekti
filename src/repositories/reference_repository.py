from sqlalchemy import text

from config import db
from entities.reference import Reference
from entities.factories import BookFormFactory, ArticleFormFactory, InproceedingsFormFactory


class ReferenceRepository:
    def __init__(self, database):
        self.db = database
        self.factories = {"book": BookFormFactory(),
                          "article": ArticleFormFactory(),
                          "inproceedings": InproceedingsFormFactory()}

    def get_references(self):
        result = self.db.session.execute(text("SELECT * FROM reference_entries"))
        references = result.mappings().all()

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

    def create_reference(self, form_data):

        columns = list(form_data.keys())
        placeholders = [f":{col}" for col in columns]

        sql = text(f"""
            INSERT INTO reference_entries
            ({', '.join(columns)})
            VALUES ({', '.join(placeholders)})
        """)

        self.db.session.execute(sql, form_data)
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
