class UserInputError(Exception):
    pass


def validate_reference(entry_type, title, authors, year):
    """
    Validates reference fields and raises an error if any field is invalid.

    Parameters:
        entry_type: The type of the reference cannot be empty.
        title: The title of the reference cannot be empty.
        authors: The authors of the reference cannot be empty.
        year: The year of the reference must be a positive number.

    Raises:
        UserInputError: If any field fails validation.
    """

    if not entry_type or len(entry_type.strip()) == 0:
        raise UserInputError("Entry type cannot be empty.")
    if not title or len(title.strip()) == 0:
        raise UserInputError("Title cannot be empty.")
    if not authors or len(authors.strip()) == 0:
        raise UserInputError("Authors field cannot be empty.")
    if not year or not str(year).isdigit() or int(year) < 0:
        raise UserInputError("Year must be a positive number.")
