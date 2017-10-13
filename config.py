class DefaultConfig(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    USER = "your-user"
    SECRET_KEY = "your-secret-key"
    DB_NAME = "your-database-name"
    SQLALCHEMY_DATABASE_URI = "postgresql://" + USER + ":" + SECRET_KEY + "@localhost/" + DB_NAME
    SQLALCHEMY_TRACK_MODIFICATIONS = True