
class Config:
    SECRET_KEY = 'secret'
    JWT_SECRET_KEY = 'secret'
    @staticmethod
    def init_app(app):
       pass

class DevelopmentConfig(Config):
    DEBUG = True
    
config = {
    'development': DevelopmentConfig
}