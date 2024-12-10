from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, validators


class BookFormFactory:
    def create_form(self, default_values=None):
        if default_values is None:
            default_values = {}
        class BookForm(FlaskForm):
            title = StringField(
                "Title",
                [validators.DataRequired()],
                default=default_values.get("title", ""),
            )
            authors = StringField(
                "Authors",
                [validators.DataRequired()],
                default=default_values.get("authors", ""),
            )
            year = IntegerField(
                "Year",
                [validators.DataRequired()],
                default=default_values.get("year", ""),
            )
            publisher = StringField(
                "Publisher", default=default_values.get("publisher", "")
            )
            isbn = StringField("ISBN", default=default_values.get("isbn", ""))

        return BookForm()


class ArticleFormFactory:
    def create_form(self, default_values=None):
        if default_values is None:
            default_values = {}
        class ArticleForm(FlaskForm):
            title = StringField(
                "Title",
                [validators.DataRequired()],
                default=default_values.get("title", ""),
            )
            authors = StringField(
                "Authors",
                [validators.DataRequired()],
                default=default_values.get("authors", ""),
            )
            year = IntegerField(
                "Year",
                [validators.DataRequired()],
                default=default_values.get("year", ""),
            )
            journal = StringField("Journal", default=default_values.get("journal", ""))
            volume = StringField("Volume", default=default_values.get("volume", ""))
            number = StringField("Number", default=default_values.get("number", ""))
            pages = StringField("Pages", default=default_values.get("pages", ""))

        return ArticleForm()


class InproceedingsFormFactory:
    def create_form(self, default_values=None):
        if default_values is None:
            default_values = {}
        class InproceedingsForm(FlaskForm):
            title = StringField(
                "Title",
                [validators.DataRequired()],
                default=default_values.get("title", ""),
            )
            booktitle = StringField("Book Title")
            authors = StringField(
                "Authors",
                [validators.DataRequired()],
                default=default_values.get("authors", ""),
            )
            year = IntegerField(
                "Year",
                [validators.DataRequired()],
                default=default_values.get("year", ""),
            )
            pages = StringField("Pages", default=default_values.get("pages", ""))
            publisher = StringField("Publisher", default=default_values.get("publisher", ""))

        return InproceedingsForm()
