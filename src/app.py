"""
This module contains routes and logic for managing references in the app.
It handles the display, creation, and deletion of references in the system.

"""

from flask import flash, jsonify, redirect, render_template, request

from config import app, test_env
from db_helper import reset_db
from repositories.reference_repository import reference_repo


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


    sort_by = request.args.get("sort", "title")  # Oletuksena "title"
    order = request.args.get("order", "asc")  # Oletuksena "asc"
    references = reference_repo.get_references(sort_by=sort_by, order=order)
    
    return render_template("index.html", references=references, sort=sort_by, order=order)


@app.route("/input-form/<reference_type>", methods=["GET"])
def get_form_fields(reference_type):
    factory = reference_repo.factories.get(reference_type)
    if not factory:
        return jsonify({"error": "Invalid reference type"}), 400

    form = factory.create_form()
    fields = [
        {
            "name": field.name,
            "label": field.label.text,
            "required": bool(field.validators),
        }
        for field in form
    ]

    return jsonify(fields)


@app.route("/bibtex")
def bibtex():
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
    return render_template("bibtex.html", references=references)


@app.route("/reference/<reference_id>", methods=["GET"])
def get_reference(reference_id):
    """
    Render the page for viewing single references
    """

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
    Gets form data in a dict, passes it to create_reference function
    
    """
    form_data = dict(request.form)

    try:
        reference_repo.create_reference(form_data)
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return redirect("/new_reference")


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
