import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')  # Got using secrets.token_hex(16) from secrets module
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
        # os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL')
    MAIL_PASSWORD = os.environ.get('PASSWORD')
