import os

# Set up the flask app
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config.from_object("default_settings.app_config")
    
    # Initialise the connection to the database
    db.init_app(app)
    
    # Initialise marshmallow
    ma.init_app(app)
    
    from commands import db_commands
    app.register_blueprint(db_commands)
    
    # register the controllers to the database
    from controllers import registerable_controllers
    for controller in registerable_controllers:
        app.register_blueprint(controller)
    
    from marshmallow.exceptions import ValidationError
    
    @app.errorhandler(ValidationError)
    def handle_bad_request(error):
        return (jsonify(error.messages), 400)
    
    return app