from base import *

DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_L7U50ZTVJ1FmVtrtUu5vZL9W')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_HN7jhITgfB0ibcCMKD13phHp')