from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

jwt = JWTManager()
db = SQLAlchemy()

def create_app(config=None):
    app = Flask(__name__)
    
    if config:
        app.config.from_object(config)

    jwt.init_app(app)
    db.init_app(app)
    CORS(app) # 解决跨域
    
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
    