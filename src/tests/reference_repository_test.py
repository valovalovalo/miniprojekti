import unittest
from unittest.mock import Mock

from entities.reference import Reference
from repositories.reference_repository import ReferenceRepository


class TestReferenceRepository(unittest.TestCase):
    def setUp(self):
        self.mock_db = Mock()
        self.mock_db.session = Mock()
        self.repo = ReferenceRepository(self.mock_db)

    def test_search_works(self):
        mock_result = Mock()
        mock_result.mappings.return_value.all.return_value = [
            {
                "id": 1,
                "entry_type": "book",
                "title": "Taru Sormusten Herrasta",
                "authors": "J.R.R Tolkien",
                "year": "1954",
            },
            {
                "id": 2,
                "entry_type": "book",
                "title": "Hobitti eli sinne ja takaisin",
                "authors": "J.R.R Tolkien",
                "year": "1937",
            },
        ]
        self.mock_db.session.execute.return_value = mock_result
        references = self.repo.get_references()

        self.mock_db.session.execute.assert_called_once()

        self.assertEqual(len(references), 2)
        self.assertIsInstance(references[0], Reference)
        self.assertEqual(references[0].data["title"], "Taru Sormusten Herrasta")
        self.assertEqual(references[1].data["authors"], "J.R.R Tolkien")

    def test_reference_creation_works(self):

        test_input = {
            "entry_type": "book",
            "title": "Vuonna 1984",
            "authors": "George Orwell",
            "year": "1949"
            }
        
        self.mock_db.session.execute.return_value.scalar.return_value = 1
        
        reference_id = self.repo.create_reference(test_input)

        self.assertEqual(reference_id, 1)

    def test_reference_delete_works(self):
        self.repo.remove_reference(1)

        self.mock_db.session.execute.assert_called_once()
        self.mock_db.session.commit.assert_called_once()

    def test_reference_update_works(self):
        test_input = {
            "entry_type": "book",
            "title": "Vuonna 1984",
            "authors": "George Orwell",
            "year": "1949"
            }
        self.repo.update_reference(1, test_input)

        self.mock_db.session.execute.assert_called_once()
        self.mock_db.session.commit.assert_called_once()
