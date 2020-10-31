from logging.config import dictConfig
from logging import DEBUG, INFO, ERROR, WARNING
import os

def config_logger(
        enable_console_handler=True, 
        enable_file_handler=True, 
        log_file='log\\app.log', 
        log_level=DEBUG,
        log_file_max_bytes=10000000, # 10MB
        log_file_max_count=5):

    # 定义输出到控制台的日志处理器
    console_handler = {
        'class': 'logging.StreamHandler',
        'formatter': 'default',
        'level': log_level,
        'stream': 'ext://flask.logging.wsgi_errors_stream'
    }
    # 定义输出到文件的日志处理器
    file_handler = {
        'class': 'logging.handlers.RotatingFileHandler',
        'formatter': 'detail',
        'filename': log_file,
        'level': log_level,
        'maxBytes': log_file_max_bytes,
        'backupCount': log_file_max_count
    }
    # 定义日志输出格式
    default_formatter = {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
    }
    detail_formatter = {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
    }
    handlers = []
    if enable_console_handler:
        handlers.append('console')
    if enable_file_handler:
        handlers.append('file')
    d = {
        'version': 1,
        'formatters': {
            'default': default_formatter,
            'detail': detail_formatter
        },
        'handlers': {
            'console': console_handler,
            'file': file_handler
        },
        'root': {
            'level': log_level,
            'handlers': handlers
        }
    }
    dictConfig(d)

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
       config_logger()

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