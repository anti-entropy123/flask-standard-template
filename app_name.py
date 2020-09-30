from app import create_app
from config import config
from flask_jwt_extended import JWTManager

app = create_app(config['development'])
jwt = JWTManager(app)

@app.shell_context_processor
def make_shell_context():
    return {'jwt': jwt}

if __name__ == "__main__":
    app.run()