from flask import Blueprint
from models.User import User
from schemas.UserSchema import user_schema

auth = Blueprint("auth", __name__, url_prefix="/auth")

@auth.route("/register", methods=["POST"])
def auth_register():
    return "working"