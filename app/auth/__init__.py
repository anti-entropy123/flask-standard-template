from flask import Blueprint
from functools import wraps
from flask_jwt_extended import get_jwt_identity
from flask import abort

# 角色权限管理装饰器, permission为所需权限
def role_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            identity = get_jwt_identity()
            print(identity, "can do this permission ?")
            # 在此处验证角色权限, 如果无对应权限, 则抛出 403
            if not permission:
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator

auth = Blueprint('auth', __name__)

from . import views