import os


class BaseConfig(object):
    DEBUG = True
    TESTING = False
    DB_SERVER = os.environ['DB_SERVER']
    MYSQL_ROOT_PASSWORD = os.environ['MYSQL_ROOT_PASSWORD']
    MYSQL_USER = os.environ['MYSQL_USER']
    MYSQL_PASSWORD = os.environ['MYSQL_PASSWORD']
    MYSQL_DATABASE = os.environ['MYSQL_DATABASE']

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return (
            f'mysql+mysqldb://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}'
            f'@{self.DB_SERVER}/{self.MYSQL_DATABASE}'
        )


class DevConfig(BaseConfig):
    pass


class ProdConfig(BaseConfig):
    DEBUG = False


class TestConfig(BaseConfig):
    TESTING = True
