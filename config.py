
import os
import sys

class Config:
    DEBUG   = False
    TESTING = False
    SECRET_KEY = '#######'
    UPLOAD_FOLDER = os.path.join(sys.path[0], 'upload')

class ProductionConfig(Config):
    pass
    
class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
