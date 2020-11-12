import os
import dotenv

dotenv.load_dotenv()

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    @property
    def SQLALCHEMY_DATABASE_URI(self):
        var = os.getenv('DB_URI')
        
        if not var:
            raise ValueError("DB_URI is not set")
        
        return var
        

class Development(Config):
    DEBUG = True

class Production(Config):
    pass

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