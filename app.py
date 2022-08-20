#!/usr/bin/env python3
# local packages
from config import app, db
from routes.home_blueprint import home_blueprint


# Create the tables that are associated with the models.
db.create_all()

app.register_blueprint(home_blueprint)

if __name__ == '__main__':
    # Main entry point when run in stand-alone mode.
    app.run(debug=True)
