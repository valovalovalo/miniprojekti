import unittest

from entities.reference import Reference


class TestReference(unittest.TestCase):

    def setUp(self):
        self.data = {
            "id": "1",
            "entry_type": "inproceedings",
            "title": "Extreme Apprenticeship Method in Teaching Programming for Beginners.",
            "authors": "Vihavainen, Arto and Paksula, Matti and Luukkainen, Matti",
            "year": 2011,
        }

    def test_get_bibtex(self):
        # Test get_bibtex() creates proper reference dict
        expected_bibtex = {
            "type": "inproceedings",
            "cite": "vihavainen2011",
            "fields": {
                "title": "Extreme Apprenticeship Method in Teaching Programming for Beginners.",
                "authors": "Vihavainen, Arto and Paksula, Matti and Luukkainen, Matti",
                "year": 2011,
            },
        }

        reference = Reference(self.data)
        assert reference.get_bibtex() == expected_bibtex
