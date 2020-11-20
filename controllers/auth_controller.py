import flask
from models.User import User
from schemas.UserSchema import user_schema
from main import db, bcrypt
import flask_jwt_extended
import datetime

auth = flask.Blueprint("auth", __name__, url_prefix="/auth")

@auth.route("/register", methods=["POST"])
def auth_register():
    response = flask.request.json
    user_fields = user_schema.load(response)
    
    user = User.query.filter_by(email=user_fields["email"]).first()
    
    if user:
        return flask.abort(400, description="email already exists")
    
    user = User()
    user.email = user_fields["email"]
    user.password = bcrypt.generate_password_hash(user_fields["password"]).decode("utf-8")
    
    db.session.add(user)
    db.session.commit()
    
    return flask.jsonify(user_schema.dump(user))
    
@auth.route("/login", methods=["POST"])
def auth_login():
    user_fields = user_schema.load(flask.request.json)
    user = User.query.filter_by(email=user_fields["email"]).first()
    
    if not user or not bcrypt.check_password_hash(user.password, user_fields["password"]):
        return flask.abort(401, "incorrect username or password")
        
    expiry = datetime.timedelta(days=1)
    access_token = flask_jwt_extended.create_access_token(identity=str(user.id), expires_delta=expiry)
    
    return flask.jsonify({"token":access_token})

@auth.route("/crash", methods=["GET"])
def auth_crash():
        import os
        os._exit(1)

