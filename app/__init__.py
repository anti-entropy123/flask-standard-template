from flask import Flask


def create_app(config=None):
    app = Flask(__name__)
    
    if config:
        app.config.from_object(config)


    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
    