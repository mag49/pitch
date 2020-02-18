import os
class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = 'maggie'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:word@localhost/pitch'
class ProdConfig(Config):
    '''
    Production configuration child class
    '''
    pass
class DevConfig(Config):
    '''
    Development configuration child class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:word@localhost/pitch'
    DEBUG = True
config_options = {
'development':DevConfig,
'production':ProdConfig
}