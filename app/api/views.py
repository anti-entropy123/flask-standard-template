from . import api
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_jwt import current_identity
from flask import jsonify
from .. import models
from ..utils import role_required

# 设置端点url和被允许的method
@api.route('/test/', methods=['GET'])
# 访问此接口需携带有效的token
@jwt_required
# 访问此接口需要的角色权限
@role_required(1)
def api_test():
    # 使用jsonify的好处是, flask会自动将content-type字段设置为 text/json
    return jsonify({'result': 1, 'message': 'its ok', 'user_id': get_jwt_identity()})

