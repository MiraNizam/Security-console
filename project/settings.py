import os
from environs import Env

env = Env()
env.read_env()

DATABASES = {
    'default': {
        'ENGINE': env.str("SECURE_ENGINE"),
        'HOST': env.str("SECURE_HOST"),
        'PORT': env.int("SECURE_PORT"),
        'NAME': env.str("SECURE_NAME"),
        'USER': env.str("SECURE_USER"),
        'PASSWORD': env.str("SECURE_PASSWORD"),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env.str("SECURE_SECRET_KEY")

DEBUG = env.bool("DEBUG")

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
