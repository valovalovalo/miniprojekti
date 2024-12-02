import unittest
from flask import Flask
from entities.factories import InproceedingsFormFactory


class TestInproceedingsFormFactory(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config["WTF_CSRF_ENABLED"] = False
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.factory = InproceedingsFormFactory()

    def test_create_form_toimii(self):
        form = self.factory.create_form()

        expected_fields = ["title","booktitle", "authors", "year", "publisher", "pages"]
        self.assertEqual(set(form._fields.keys()), set(expected_fields))
