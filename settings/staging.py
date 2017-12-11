from base import *

DEBUG = False


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_L7U50ZTVJ1FmVtrtUu5vZL9W')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_HN7jhITgfB0ibcCMKD13phHp')

SITE_URL = 'https://share-respite.herokuapp.com'
ALLOWED_HOSTS.append('share-respite.herokuapp.com')

# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}