from app import create_app
from config import config
from app import jwt

app = create_app(config['development'])

@app.shell_context_processor
def make_shell_context():
    return {'jwt': jwt}

if __name__ == "__main__":
    app.run()