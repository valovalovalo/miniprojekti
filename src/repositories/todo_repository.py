from config import db
from sqlalchemy import text

from entities.todo import Todo

def get_todos():
    result = db.session.execute(text("SELECT content, done FROM todos"))
    todos = result.fetchall()
    return [Todo(todo[0], todo[1]) for todo in todos] 

def create_todo(content):
    sql = text("INSERT INTO todos (content) VALUES (:content)")
    db.session.execute(sql, { "content": content })
    db.session.commit()
