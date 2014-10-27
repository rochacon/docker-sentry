# /etc/sentry.conf.py
# edit this to your liking
import os

import dj_database_url


DATABASES = {'default': dj_database_url.config()}

# No trailing slash!
SENTRY_URL_PREFIX = 'http://127.0.0.1.xip.io'  # FIXME modify this to your domain

# SENTRY_KEY is a unique randomly generated secret key for your server, and it
# acts as a signing token
SENTRY_KEY = '0123456789abcde'  # FIXME modify this to an unique key

SENTRY_WEB_HOST = '0.0.0.0'
SENTRY_WEB_PORT = 9000
SENTRY_WEB_OPTIONS = {
    'workers': 3,  # the number of gunicorn workers
    'secure_scheme_headers': {'X-FORWARDED-PROTO': 'https'},  # detect HTTPS mode from X-Forwarded-Proto header
}

_redis_endpoint = os.environ.get('REDIS_ENDPOINT', '127.0.0.1:6379')
SENTRY_REDIS_OPTIONS = {
    'hosts': {
        0: {
            'host': _redis_endpoint.split(':')[0],
            'port': _redis_endpoint.split(':')[1],
        }
    }
}

# TODO
#EMAIL_HOST = 'localhost'
#EMAIL_HOST_PASSWORD = ''
#EMAIL_HOST_USER = ''
#EMAIL_PORT = 25
#EMAIL_USE_TLS = False

ALLOWED_HOSTS = ['*']
