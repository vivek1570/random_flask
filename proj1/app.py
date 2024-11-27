import sqlite3
from flask import render_template,Flask

app=Flask(__name__)

@app.route('/')
def index():
  conn=get_db_connection()
  posts=conn.execute('SELECT * FROM posts').fetchall()
  conn.close()
  return render_template('index.html',posts=posts)

def get_db_connection():
  conn=sqlite3.connect('database.db')
  conn.row_factory=sqlite3.Row
  return conn