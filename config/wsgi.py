import os
from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv
load_dotenv()

environment = os.getenv('ENVIRONMENT')

if environment == 'production':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')
elif environment == 'staging':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.staging')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')

application = get_wsgi_application()
