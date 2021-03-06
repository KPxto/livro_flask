import os
import random, string


class Config(object):
    CSRF_ENABLED = True
    SECRET = "ysb_92=qe#dgjf8%0ng+a*#4rt#5%3*4kw5%i2bck*gn@w3@f&-&"
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    APP = None
    SQLALCHEMY_DATABASE_URI = "mysql://root:25123436@localhost:3306/livro_flask"


class DevelopmentConfig(Config):
    TETSING = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN = f'http://{IP_HOST}:{PORT_HOST}/'


class TestingConfig(Config):
    TETSING = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 5000
    URL_MAIN = f'http://{IP_HOST}:{PORT_HOST}/'


class ProductionConfig(Config):
    TETSING = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8080
    URL_MAIN = f'http://{IP_HOST}:{PORT_HOST}/'


app_config = {
    'development': DevelopmentConfig(),
    'testing': TestingConfig(),
    'production': ProductionConfig()
}


app_active = os.getenv('FLASK_ENV')
