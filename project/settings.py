import os
from dotenv import load_dotenv

load_dotenv()
DATABASES = {
    'default': {
        'ENGINE': os.environ["SECURE_ENGINE"],
        'HOST': os.environ["SECURE_HOST"],
        'PORT': os.environ["SECURE_PORT"],
        'NAME': os.environ["SECURE_NAME"],
        'USER': os.environ["SECURE_USER"],
        'PASSWORD': os.environ["SECURE_PASSWORD"],
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.environ["SECURE_SECRET_KEY"]

DEBUG = True

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
