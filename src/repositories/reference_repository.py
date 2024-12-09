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


    def get_references(self, sort_by="title", order="asc"):
        """
        Fetch references from the database with sorting.

        Args:
            sort_by (str): Column to sort by (e.g., 'title', 'authors', 'year').
            order (str): Sort order ('asc' for ascending, 'desc' for descending).

        Returns:
            List[Reference]: List of Reference objects.
        """

        if sort_by not in {"title", "authors", "year"}:
            sort_by = "title"

        if order not in {"asc", "desc"}:
            order = "asc"

        sql = text(f"""
            SELECT * FROM reference_entries
            ORDER BY {sort_by} {order}
        """)

        result = self.db.session.execute(sql)
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
        """
        Function for creating a reference

        """

        columns = list(form_data.keys())
        placeholders = [f":{col}" for col in columns]

        sql = text(f"""
            INSERT INTO reference_entries
            ({', '.join(columns)})
            VALUES ({', '.join(placeholders)})
        """)

        self.db.session.execute(sql, form_data)
        self.db.session.commit()


    def update_reference(self, reference_id, form_data):
        """
        Function for updating a reference
        """

        columns = list(form_data.keys())
        placeholders = [f":{col}" for col in columns]


        # Maybe works...
        sql = text(f"""
            UPDATE reference_entries
            SET {', '.join([f"{col} = {placeholder}" for col, placeholder in zip(columns, placeholders)])}
            WHERE id = (:reference_id)
        """)

        self.db.session.execute(sql, form_data, {"reference_id":reference_id})
        self.db.session.commit()
        

    def remove_reference(self, reference_id):
        """
        Function for removing a reference from the database
        """
        
        sql = text(
            """
            DELETE FROM reference_entries WHERE id = :id
            """
        )

        self.db.session.execute(sql, {"id": reference_id})
        self.db.session.commit()


reference_repo = ReferenceRepository(db)
