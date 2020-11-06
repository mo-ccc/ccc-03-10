import os

# Set up the flask app
from flask import Flask
app = Flask(__name__)

# Initialise the connection to the database
from database import init_db
db = init_db(app)

# Set up marshmallow to handle serialization/deserialization
from flask_marshmallow import Marshmallow
ma = Marshmallow(app)

# register the controllers to the database
from controllers import registerable_controllers
for controller in registerable_controllers:
    app.register_blueprint(controller)
