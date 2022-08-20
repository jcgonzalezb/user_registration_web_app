# flask packages
from flask import Blueprint, render_template, request
import sqlite3 as sql

new_user_blueprint = Blueprint('new_user_blueprint', __name__, url_prefix='/new_user')

@new_user_blueprint.route('/', methods=['POST', 'GET'], strict_slashes=False)
def new_user():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            city = request.form['city']

            with sql.connect("users.db") as con:
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO users (name,email,city) VALUES (?,?,?)",
                    (name, email, city))

                con.commit()
                msg = "Record successfully added"
                con.close()
                return render_template("result.html", msg=msg)
        except:
            con.rollback()
            msg = "error in insert operation"
