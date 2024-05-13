from .common import *
import dj_database_url
from django_on_heroku import settings as heroku_settings

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

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/'),
]

AWS_STORAGE_BUCKET_NAME = 'remote-forge'
AWS_S3_REGION_NAME = 'eu-west-1'

AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')
AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY', '')

# AWS_S3_USE_SSL = True
# AWS_S3_VERIFY = True
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'

# STATICFILES_STORAGE = 'custom_storages.StaticStorage'
# STATICFILES_LOCATION = 'static'
# DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
# MEDIAFILES_LOCATION = 'media'

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


