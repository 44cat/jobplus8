class BaseConfig(object):
    SECRET_KEY = 'very secret key'
    INDEX_PER_PAGE = 9
    ADMIN_PER_PAGE = 15
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    #SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@localhost:5000/jobplus8'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@localhost:5000/jobplus8?charset=utf8'

class ProductionConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    pass


configs = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
