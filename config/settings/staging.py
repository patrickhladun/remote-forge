from .common import *
import dj_database_url
from django_on_heroku import settings as heroku_settings
from dotenv import load_dotenv, find_dotenv
load_dotenv(BASE_DIR / '.env')
heroku_settings(locals(), staticfiles=False)

DEBUG = True
ALLOWED_HOSTS = [
    '0.0.0.0', 
    'localhost', 
    '127.0.0.1', 
    'remote-forge-staging-b6cedb8831c2.herokuapp.com'
]
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL')),
}
SECRET_KEY = os.getenv('SECRET_KEY', '')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/'),
]
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'remote-forge-s3bkt'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_FILE_OVERWRITE = False
AWS_S3_REGION_NAME = 'eu-west-1'
AWS_DEFAULT_ACL = 'public-read'
AWS_QUERYSTRING_AUTH = False
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
STATICFILES_LOCATION = 'static'
MEDIAFILES_LOCATION = 'media'
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
    },
}