import os

class Config(object):
    SECRET_KEY = os.environ.get('IoDDW1PoKh&$lQ0@^pj6msL#YTVVwAJFFoZpO*m8n1&7') 
    MONGODB_SETTINGS = { 'db':'uta_enrollment'}
    SQLALCHEMY_DATABASE_URI = 'mysql://Terry:I0t@C0d3sling3r@localhost/uta'
    SQLALCHEMY_ECHO = True  
    SQLALCHEMY_TRACK_MODIFICATIONS = True