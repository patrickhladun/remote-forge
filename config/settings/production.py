from .common import *
import dj_database_url

DEBUG = False
ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1', 'remote-forge-9e36fbf11ce1.herokuapp.com']
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL')),
}
SECRET_KEY = os.getenv('SECRET_KEY')