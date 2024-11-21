import unittest
from util import validate_reference, UserInputError

class TestReferenceValidation(unittest.TestCase):
    """
    Testiluokka, joka testaa validate_reference-funktion toimivuutta.
    Tämä luokka sisältää testejä, jotka varmistavat, että 
    syötteiden pituus on oikein ja virheet käsitellään odotetulla tavalla.
    
    """
    def test_valid_length_does_not_raise_error(self):
        """
        Testaa, että validate_reference ei nosta virhettä, kun syöte on 
        hyväksyttävän pituinen (5-100 merkkiä).
        
        """
        try:
            validate_reference("Valid Title")
            validate_reference("A" * 5)
            validate_reference("A" * 100)
        except UserInputError as e:
            self.fail(f"validate_reference raised UserInputError unexpectedly: {e}")

    def test_too_short_raises_error(self):
        
        """
        Testaa, että validate_reference nostaa UserInputError-virheen, 
        jos syöte on liian lyhyt (alle 5 merkkiä).
        
        """

        with self.assertRaises(UserInputError):
            validate_reference("A")
        
        with self.assertRaises(UserInputError):
            validate_reference("")

        with self.assertRaises(UserInputError):
            validate_reference("1234")

    def test_too_long_raises_error(self):

        with self.assertRaises(UserInputError):
            validate_reference("A" * 101)

        with self.assertRaises(UserInputError):
            validate_reference("B" * 1000)

if __name__ == "__main__":
    unittest.main()

