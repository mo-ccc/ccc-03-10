import flask_jwt_extended
import flask
from models.User import User
from functools import wraps

def verify_user(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user_id = flask_jwt_extended.get_jwt_identity()
        user = User.query.get(user_id)
        
        if not user:
            return flask.abort(401, description="Invalid user")
        
        return func(*args, user=user, **kwargs)
    
    return wrapper
    
    
    