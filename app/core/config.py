import os
from typing import Literal


class BaseConfig:
    DEBUG = False
    TESTING = False


class ProdConfig(BaseConfig):
    DB_SERVER = os.environ.get('DB_SERVER', 'db')
    MYSQL_ROOT_PASSWORD = os.environ['MYSQL_ROOT_PASSWORD']

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return (
            f'mysql+mysqldb://root:{self.MYSQL_ROOT_PASSWORD}'
            f'@{self.DB_SERVER}/todo'
        )


class DevConfig(ProdConfig):
    DEBUG = True


class TestConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./test.db'


def get_config(config_name: Literal['PROD', 'DEV', 'TEST']) -> BaseConfig:
    CONFIG = {
        'PROD': ProdConfig,
        'DEV': DevConfig,
        'TEST': TestConfig,
    }
    return CONFIG[config_name]()
