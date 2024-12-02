from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators


class BookFormFactory:
    def create_form(self):
        class BookForm(FlaskForm):
            title = StringField("Title", [validators.DataRequired()])
            authors = StringField("Authors", [validators.DataRequired()])
            year = IntegerField("Year", [validators.DataRequired()])
            publisher = StringField("Publisher")
            isbn = StringField("ISBN")

        return BookForm()


class ArticleFormFactory:
    def create_form(self):
        class ArticleForm(FlaskForm):
            title = StringField("Title", [validators.DataRequired()])
            authors = StringField("Authors", [validators.DataRequired()])
            year = IntegerField("Year", [validators.DataRequired()])
            journal = StringField("Journal")
            volume = StringField("Volume")
            number = StringField("Number")
            pages = StringField("Pages")

        return ArticleForm()

class InproceedingsFormFactory:
    def create_form(self):
        class InproceedingsForm(FlaskForm):
            title = StringField("Title", [validators.DataRequired()])
            booktitle = StringField("Book Title")
            authors = StringField("Authors", [validators.DataRequired()])
            year = IntegerField("Year", [validators.DataRequired()])
            pages = StringField("Pages")
            publisher = StringField("Publisher")

        return InproceedingsForm()
