class BaseConfig(object):
    DEBUG = True
    TESTING = False
    DB_SERVER = 'localhost'

    @property
    def DATABASE_URI(self):
        return f'mysql://user@{self.DB_SERVER}/todo'


class DevConfig(BaseConfig):
    pass


class ProdConfig(BaseConfig):
    DEBUG = False
    DB_SERVER = 'db'
