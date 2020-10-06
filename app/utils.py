from functools import wraps
from flask_jwt_extended import get_jwt_identity
from flask import abort

def role_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            identity = get_jwt_identity()
            print(identity, "can do this permission ?")
            if not permission:
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator