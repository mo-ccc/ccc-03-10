import flask
from models.User import User
from schemas.UserSchema import user_schema
from main import db, bcrypt

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