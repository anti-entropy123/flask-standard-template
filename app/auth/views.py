from flask import request, jsonify
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_refresh_token_required, create_refresh_token
from . import auth

@auth.route('/login/', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if username != 'test' or password != 'test': 
        return jsonify(msg="Bad username or password"), 401

    access_token = create_access_token(identity=username)
    refresh_token = create_refresh_token(identity=username)
    return jsonify(access_token=access_token, refresh_token=refresh_token)

@auth.route('/refresh/', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    return jsonify(access_token=create_access_token(identity=current_user)), 200