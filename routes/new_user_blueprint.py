# flask packages
from flask import Blueprint, render_template, request
import sqlite3 as sql

# project resources
from config import app


@app.route('/new_user', methods=['POST', 'GET'])
def new_user():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            city = request.form['city']

            with sql.connect("users.db") as con:
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO students (name,email,city) VALUES (?,?,?)",
                    (name, email, city))

                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("result.html", msg=msg)
            con.close()
