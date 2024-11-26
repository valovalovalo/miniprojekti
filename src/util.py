class UserInputError(Exception):
    pass

def validate_reference(entry_type, title, authors, year):
    if not entry_type or len(entry_type.strip()) == 0:
        raise UserInputError("Entry type cannot be empty.")
    if not title or len(title()) == 0:
        raise UserInputError("Title cannot be empty.")
    if not authors or len(authors.strip()) == 0:
        raise UserInputError("Authors field cannot be empty.")
    if not year or not str(year).isdigit() or int(year) < 0:
        raise UserInputError("Year must be a positive number.")