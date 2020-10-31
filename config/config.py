
class Config:
    # 密钥, 用于session, cookie等
    SECRET_KEY = 'secret'
    # 密钥, 用于生成加密jwt token
    JWT_SECRET_KEY = 'secret'
    # cors字段
    CORS_ORIGINS = '*'
    # cors字段
    CORS_SUPPORTS_CREDENTIALS = True
    # sql数据库url
    SQLALCHEMY_DATABASE_URI = 'DBMS://USERNAME:PASSWORD@HOST_ADD/db_name'
    # 关闭对象变化跟踪, 以节省开销
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    # 如果需要的话, 在此函数中进行其它的配置
    def init_app(app):
       pass

class DevelopmentConfig(Config):
    DEBUG = True # 调试模式
    JWT_ACCESS_TOKEN_EXPIRES = False # 不会过期(不推荐)
    JWT_REFRESH_TOKEN_EXPIRES = False # 不会过期(不推荐)

class ProductionConfig(Config):
    JWT_ACCESS_TOKEN_EXPIRES = 3600 # token有效期为1个小时

config = {
    'development': DevelopmentConfig, # 开发环境配置
    'production': ProductionConfig    # 生产环境配置
}