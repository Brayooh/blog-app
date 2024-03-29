import os

from dotenv import load_dotenv as ld

ld()


class Config:
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://brayooh:brian@localhost/blog'
    SECRET_KEY='qwertyuiop'
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SENDGRID_API_KEY=os.environ.get('SENDGRID_API_KEY')
    DEFAULT_SENDGRID_SENDER =  os.environ.get('DEFAULT_SENDGRID_SENDER')

    debug = True

    #  email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://brayooh:brian@localhost/blog'


config_options = {
   'development': DevConfig,
   'production': ProdConfig,
}