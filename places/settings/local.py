from .base import *
import sys

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

TESTING = 'test' in sys.argv

if TESTING:
    PASSWORD_HASHERS = [
        'django.contrib.auth.hashers.MD5PasswordHasher',
    ]