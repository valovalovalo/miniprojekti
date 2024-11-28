class Reference:
    def __init__(self, id, entry_type, title, authors, year):
        self.id = id
        self.entry_type = entry_type
        self.title = title
        self.authors = authors
        self.year = year
        self.bibtext = self.get_bibtext()

    def get_bibtext(self):
        first_author = self.authors.split(",")[0].strip().split()[-1]
        cite = f"{first_author.lower()}{self.year}"
        
        fields = {
            "title": self.title,
            "author": self.authors,
            "year": self.year
        }

        bibtext = {
            "type": self.entry_type,
            "cite": cite,
            "fields": fields
        }

        return bibtext

    def __str__(self):
        first_author = self.authors.split(",")[0].strip().split()[-1]
        citation_key = f"{first_author.lower()}{self.year}"

        return (
            f"@{self.entry_type}{{{citation_key},\n"
            f"  title = {{{self.title}}},\n"
            f"  author = {{{self.authors}}},\n"
            f"  year = {{{self.year}}}\n"
            "}"
        )
