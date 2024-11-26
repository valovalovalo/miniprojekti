import unittest
from util import validate_reference, UserInputError

class TestValidateReference(unittest.TestCase):
    def setUp(self):
        self.valid_entry_type = "book"
        self.valid_title = "A Valid Title"
        self.valid_authors = "Author Name"
        self.valid_year = 2023

    def test_valid_reference_does_not_raise_error(self):
        try:
            validate_reference(
                self.valid_entry_type,
                self.valid_title,
                self.valid_authors,
                self.valid_year
            )
        except UserInputError as error:
            self.fail(f"Unexpected error: {error}")

    def test_empty_entry_type_raises_error(self):
        with self.assertRaises(UserInputError) as c:
            validate_reference("", self.valid_title, self.valid_authors, self.valid_year)
        self.assertEqual(str(c.exception), "Entry type cannot be empty.")

    def test_empty_title_raises_error(self):
        with self.assertRaises(UserInputError) as c:
            validate_reference(self.valid_entry_type, "", self.valid_authors, self.valid_year)
        self.assertEqual(str(c.exception), "Title cannot be empty.")

    def test_empty_authors_raises_error(self):
        with self.assertRaises(UserInputError) as c:
            validate_reference(self.valid_entry_type, self.valid_title, "", self.valid_year)
        self.assertEqual(str(c.exception), "Authors field cannot be empty.")

    def test_invalid_year_raises_error(self):
        with self.assertRaises(UserInputError) as c:
            validate_reference(self.valid_entry_type, self.valid_title, self.valid_authors, "abc")
        self.assertEqual(str(c.exception), "Year must be a positive number.")

        with self.assertRaises(UserInputError) as c:
            validate_reference(self.valid_entry_type, self.valid_title, self.valid_authors, -2023)
        self.assertEqual(str(c.exception), "Year must be a positive number.")

if __name__ == "__main__":
    unittest.main()
