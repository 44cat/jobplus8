class BaseConfig(object):
    """   配置基类   """
    SECRET_KEY = 'very secret key'
    INDEX_PER_PAGE = 4
    ADMIN_PER_PAGE = 8
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    """   开发环境配置   """
    DEBUG = True
    #SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@localhost:5000/jobplus8'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@localhost:5000/jobplus8?charset=utf8'

class ProductionConfig(BaseConfig):
    """ 生产环境配置 """
    pass


class TestingConfig(BaseConfig):
    """ 测试环境配置 """
    pass


configs = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
