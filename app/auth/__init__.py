from flask import Blueprint
from functools import wraps
from flask_jwt_extended import get_jwt_identity
from flask import abort

auth = Blueprint('auth', __name__)

from . import views