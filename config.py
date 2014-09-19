
import os
import sys

class Config:
    DEBUG   = False
    TESTING = False
    SECRET_KEY = '?\xbf,\xb4\x8d\xa3"<\x9c\xb0@\x0f5\xab,w\xee\x8d$0\x13\x8b83'
    UPLOAD_FOLDER = os.path.join(sys.path[0], 'upload')

class ProductionConfig(Config):
    pass
    
class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
