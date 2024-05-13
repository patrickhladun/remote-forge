from .common import *
import dj_database_url

DEBUG = False
ALLOWED_HOSTS = [
    '0.0.0.0', 
    'localhost', 
    '127.0.0.1', 
    'remote-forge-9e36fbf11ce1.herokuapp.com'
]
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL')),
}
SECRET_KEY = os.getenv('SECRET_KEY', '')
EXTERNAL_APPS+=['storages']
AWS_STORAGE_BUCKET_NAME = 'remote-forge'
AWS_S3_REGION_NAME = 'eu-west-1'
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATICFILES_LOCATION = 'static'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
MEDIAFILES_LOCATION = 'media'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'