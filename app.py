#!/usr/bin/env python3
# local packages
from config import app, db
from routes.home_blueprint import home_blueprint
from routes.new_user_blueprint import new_user_blueprint
from routes.user_list_blueprint import user_list_blueprint

from flask import render_template

# Create the tables that are associated with the models.
db.create_all()

app.register_blueprint(home_blueprint)

@app.route('/enternew')
def add_user():
   return render_template('new_user.html')

app.register_blueprint(new_user_blueprint)
app.register_blueprint(user_list_blueprint)

if __name__ == '__main__':
    # Main entry point when run in stand-alone mode.
    app.run(debug=True)
