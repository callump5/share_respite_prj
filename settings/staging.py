from base import *
import dj_database_url

DEBUG = False


# Load the ClearDB connection details from the environment variable
DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
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