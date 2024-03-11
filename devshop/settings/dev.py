from .common import *


DEBUG = True

SECRET_KEY = 'django-insecure-0@7(e9#(k$nd*ozzk0rs0fmv@vgk(hjvs=c@ei!4m%-v&7pmg7'

if DEBUG:
    MIDDLEWARE += ['silk.middleware.SilkyMiddleware']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'devshop',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': os.environ['DB_PASSWORD']
    }
}
