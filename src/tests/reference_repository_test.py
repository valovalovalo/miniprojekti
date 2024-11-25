import unittest
from unittest.mock import Mock, patch

from entities.reference import Reference


class TestReferenceRepository(unittest.TestCase):
    def setUp(self):
        self.mock_db = Mock()
        self.mock_db.session = Mock()

        from repositories.reference_repository import ReferenceRepository
        self.repo = ReferenceRepository(self.mock_db)


    def test_testi_toimii(self):
        self.assertEqual(0,0)

    def test_haku_toimii(self):
        mock_result = Mock()
        mock_result.fetchall.return_value = [
            [1, 'book', 'Taru Sormusten Herrasta', 'J.R.R Tolkien', '1954'],
            [2, 'book', 'Hobitti eli sinne ja takaisin', 'J.R.R Tolkien', '1937']
        ]
        self.mock_db.session.execute.return_value = mock_result
        references = self.repo.get_references()

        self.mock_db.session.execute.assert_called_once()
