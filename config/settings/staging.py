from .common import *
import dj_database_url

DEBUG = True
ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1', 'remote-forge-staging-b6cedb8831c2.herokuapp.com']
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL')),
}
SECRET_KEY = os.getenv('SECRET_KEY')