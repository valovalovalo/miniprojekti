from flask import redirect, render_template, request, jsonify
from db_helper import reset_db, setup_db
from repositories.todo_repository import get_todos, create_todo

from setup import app, test_env

@app.route("/")
def index():
    todos = get_todos()
    unfinished = len([todo for todo in todos if not todo.done])
    return render_template("index.html", todos=todos, unfinished=unfinished) 

@app.route("/new_todo")
def new():
    return render_template("new_todo.html")

@app.route("/create_todo", methods=["POST"])
def todo_creation():
    content = request.form.get("content")
    create_todo(content)

    return redirect("/")

    #try:
    #    user_service.check_credentials(username, password)
    #    return redirect_to_ohtu()
    #except Exception as error:
    #    flash(str(error))
    #    return redirect_to_login()

# testausta varten olevat reitit
if test_env:
    @app.route("/setup_db")
    def setup_database():
        setup_db()
        print("setup db")
        return jsonify({ 'message': "db setup done" })

    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
