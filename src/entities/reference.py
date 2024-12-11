class Reference:
    def __init__(self, data):
        self.data = data
        self.bibtex = self.get_bibtex()

    def get_data(self):
        return self.data

    def get_bibtex(self):
        first_author = self.data["authors"].split(",")[0].strip().split()[-1]
        cite = f'{first_author.lower()}{self.data["year"]}'

        data_fields = [
            "title",
            "authors",
            "year",
            "publisher",
            "isbn",
            "editor",
            "month",
            "journal",
            "volume",
            "number",
            "pages",
            "booktitle",
        ]

        fields = {}

        for field in data_fields:
            value = self.data.get(field)
            if value:
                fields[field] = value

        bibtex = {"type": self.data["entry_type"], "cite": cite, "fields": fields}

        return bibtex
