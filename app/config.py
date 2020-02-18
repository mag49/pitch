import os
class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = 'fello'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://maggie:queen@localhost/pitch'
class ProdConfig(Config):
    '''
    Production configuration child class
    '''
    pass
class DevConfig(Config):
    '''
    Development configuration child class
    '''
    DEBUG = True
config_options = {
'development':DevConfig,
'production':ProdConfig
}