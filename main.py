import os

# Set up the flask app
from flask import Flask
app = Flask(__name__)
app.config.from_object("default_settings.app_config")

# Initialise the connection to the database
from database import init_db
db = init_db(app)

# Set up marshmallow to handle serialization/deserialization
from flask_marshmallow import Marshmallow
ma = Marshmallow(app)

from commands import db_commands
app.register_blueprint(db_commands)

# register the controllers to the database
from controllers import registerable_controllers
for controller in registerable_controllers:
    app.register_blueprint(controller)

from flask import jsonify
from marshmallow.exceptions import ValidationError

@app.errorhandler(ValidationError)
def handle_bad_request(error):
    return (jsonify(error.messages), 400)