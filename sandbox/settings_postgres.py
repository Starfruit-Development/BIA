from settings import *  # noqa

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bia_lona_antincendios',
        'USER': 'bia_bombero',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}
