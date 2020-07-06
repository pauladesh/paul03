import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine("postgresql://postgres:2503@localhost:5432/marigold")
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    teachers = db.execute("SELECT * FROM teachers").fetchall()
    return render_template("index.html", teachers=teachers)

@app.route("/admission", methods=["POST"])
def admission():
    """add a student"""

    # Get form information.
    s_name = request.form.get("s_name")
    try:
        t_id = int(request.form.get("t_id"))
    except ValueError:
        return render_template("error.html", message="Invalid teacher's ID")

    # Make sure the teacher exists.
    if db.execute("SELECT * FROM teachers WHERE id = :id", {"id": t_id}).rowcount == 0:
        return render_template("error.html", message="No such teacher with that id.")
    db.execute("INSERT INTO students (s_name, t_id) VALUES (:s_name, :t_id)",
            {"s_name": s_name, "t_id": t_id})    #from line 22 and line 24
    db.commit()
    return render_template("success.html")

if __name__=='__main__':
    app.run(debug=True)
