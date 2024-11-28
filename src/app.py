from flask import flash, jsonify, redirect, render_template, request

from config import app, test_env
from db_helper import reset_db
from repositories.reference_repository import reference_repo
from util import validate_reference


@app.route("/")
def index():
    """
    Render the index page.

    ---

    Fetches all references from the database using `get_references` and
    passes them to the "index.html" template for rendering.

    ---

    Returns:
        Response: Rendered HTML page with a list of references.
    """

    references = reference_repo.get_references()
    return render_template("index.html", references=references)

@app.route("/bibtext")
def bibtext():

    """
    Render the bibtex page.

    ---

    Fetches all references from the database using `get_references` and 
    passes them to the "bibtex.html" template for rendering.

    ---

    Returns:
        Response: Rendered HTML page with a list of references.
    """

    references = reference_repo.get_references()
    return render_template("bibtext.html", references=references)


@app.route("/reference/<reference_id>", methods=["POST", "GET"])
def reference(reference_id):
    """
    Render the page for viewing single references
    """

    if request.method == "GET":
        reference = reference_repo.get_reference_by_id(reference_id)

        return render_template("reference.html", reference=reference[0])

@app.route("/new_reference")
def new():
    """
    Render the page for creating a new reference.

    ---

    Renders the "new_reference.html" template where users can input details
    for creating a new reference.

    ---

    Returns:
        Response: Rendered HTML page for creating a new reference.
    """

    return render_template("new_reference.html")


@app.route("/create_reference", methods=["POST"])
def reference_creation():
    """
    Handle the creation of a new reference.

    ---

    Retrieves reference data from the request form, validates it, and
    creates a new reference in the database. Redirects to the home page on
    success or back to the new reference page on failure.

    ---

    Methods:
        POST: Accepts data for the new reference from an HTML form.

    Returns:

        Response: Redirect to the home page ("/") on success, or to
                  "/new_reference" with an error message on failure.
    """

    entry_type = request.form.get("entry_type")
    title = request.form.get("title")
    authors = request.form.get("authors")
    year = request.form.get("year")

    try:
        validate_reference(entry_type, title, authors, year)
        reference_repo.create_reference(entry_type, title, authors, year)
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return redirect("/new_reference")


@app.route("/update_reference/<reference_id>", methods=["POST"])
def update_reference(reference_id):
    """
    Not implemented yet.
    """

    return redirect("/")

@app.route("/remove_reference/<reference_id>", methods=["POST"])
def remove_reference(reference_id):
    try:
        reference_repo.remove_reference(reference_id)
        flash("Viite poistettu onnistuneesti!")
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return redirect("/")


# testausta varten oleva reitti
if test_env:

    @app.route("/reset_db")
    def reset_database():
        """
        Reset the database (for testing purposes only).

        ---

        Clears the database by calling `reset_db` and returns a success
        message in JSON format. Only available in testing environments.

        ---

        Returns:
            Response: JSON object with a success message.
        """
        reset_db()

        return jsonify({"message": "db reset"})
    