import os
from typing import Literal


class BaseConfig:
    DEBUG = False
    TESTING = False


class ProdConfig(BaseConfig):
    DB_SERVER = os.environ.get('DB_SERVER', 'db')
    MYSQL_USER = os.environ.get('MYSQL_USER')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
    MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE')

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return (
            f'mysql+mysqldb://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}'
            f'@{self.DB_SERVER}/{self.MYSQL_DATABASE}'
        )


class DevConfig(ProdConfig):
    DEBUG = True
    MYSQL_USER = os.environ.get('MYSQL_USER', 'user')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'YES')
    MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE', 'todo')


class TestConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'


def get_config(config_name: Literal['PROD', 'DEV', 'TEST']) -> BaseConfig:
    CONFIG = {
        'PROD': ProdConfig,
        'DEV': DevConfig,
        'TEST': TestConfig,
    }
    return CONFIG[config_name]()
