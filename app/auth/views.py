from flask import request, jsonify
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_refresh_token_required, create_refresh_token
from . import auth

@auth.route('/login/', methods=['POST'])
def login():
    user_id = request.json.get('user_id', None)
    password = request.json.get('password', None)

    # 此处验证用户身份
    if user_id != 'test' or password != 'test': 
        return jsonify(msg="Bad user_id or password"), 401

    access_token = create_access_token(identity=user_id)
    refresh_token = create_refresh_token(identity=user_id)
    return jsonify(access_token=access_token, refresh_token=refresh_token)

@auth.route('/refresh/', methods=['POST'])
# 访问此接口需要携带有效的refresh_token
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    return jsonify(access_token=create_access_token(identity=current_user)), 200