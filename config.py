import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '' 
    #fill'' with random key of your choice
