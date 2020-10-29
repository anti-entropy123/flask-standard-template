from app import create_app
from config import config
from app import jwt
from app import db

# 调用工程函数构建应用实例
app = create_app(config['development'])

# flask shell 构建上下文
@app.shell_context_processor
def make_shell_context():
    return {
        'jwt': jwt,
        'db': db
    }

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=8000,
        # 仅使用https时需要
        # ssl_context=('cert/server.crt', 'cert/server.key')
    )