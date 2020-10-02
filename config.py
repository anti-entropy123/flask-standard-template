
class Config:
    SECRET_KEY = 'secret'
    JWT_SECRET_KEY = 'secret'
    CORS_ORIGINS = '*'
    CORS_SUPPORTS_CREDENTIALS = True
    @staticmethod
    def init_app(app):
       pass

class DevelopmentConfig(Config):
    DEBUG = True
    JWT_ACCESS_TOKEN_EXPIRES = False # 不会过期(不推荐)
    JWT_REFRESH_TOKEN_EXPIRES = False

class ProductionConfig(Config):
    JWT_ACCESS_TOKEN_EXPIRES = 3600

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}