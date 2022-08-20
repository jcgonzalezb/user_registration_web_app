# flask packages
from flask import Blueprint, render_template, request
import sqlite3 as sql

user_list_blueprint = Blueprint('user_list_blueprint', __name__, url_prefix='/user_list')

@user_list_blueprint.route('/', strict_slashes=False)
def list():
   con = sql.connect("users.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from users")
   
   rows = cur.fetchall()
   return render_template("user_list.html",rows = rows)
