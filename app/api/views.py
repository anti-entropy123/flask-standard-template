from . import api
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_jwt import current_identity
from flask import jsonify

@api.route('/test/', methods=['GET'])
@jwt_required
def api_test():
    return jsonify({'result': 1, 'message': 'its ok', 'username': get_jwt_identity()})