import os
import dotenv

dotenv.load_dotenv()

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('SECRET_KEY')
    MAX_CONTENT_LENGTH = 1 * 1024 * 1024

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        var = os.getenv('DB_URI')
        
        if not var:
            raise ValueError("DB_URI is not set")
        
        return var
    
    @property
    def AWS_ACCESS_KEY_ID(self):
        value = os.environ.get("AWS_ACCESS_KEY_ID")

        if not value:
            raise ValueError("AWS_ACCESS_KEY_ID is not set")

        return value
    
    @property
    def AWS_SECRET_ACCESS_KEY(self):
        value = os.environ.get("AWS_SECRET_ACCESS_KEY")

        if not value:
            raise ValueError("AWS_SECRET_ACCESS_KEY is not set")

        return value
    
    @property
    def AWS_S3_BUCKET(self):
        value = os.environ.get("AWS_S3_BUCKET")

        if not value:
            raise ValueError("AWS_S3_BUCKET is not set")

        return value
        

class Development(Config):
    DEBUG = True

class Production(Config):
    @property
    def JWT_SECRET_KEY(self):
        var = os.getenv("JWT_SECRET_KEY")
        
        if not var:
            raise ValueError("JWT_SECRET_KEY is not set")
        
        return var

class Testing(Config):
    TESTING = True
    
environment = os.getenv("FLASK_ENV")

if environment == 'production':
    app_config = Production()
    
elif environment == 'development':
    app_config = Development()
    
elif environment == 'testing':
    app_config = Testing()
    
else:
    raise ValueError('false environment variable for FLASK_ENV')