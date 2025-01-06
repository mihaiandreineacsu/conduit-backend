"""
Django container-specific settings for the conduit project.

This file serves as a configuration layer for Django when running inside a Docker container.
It is designed to extend the base `settings.py` file by overriding or adding settings specific
to the containerized environment. This approach allows for separation of concerns, making it
easier to manage settings for different environments (e.g., local development, production, testing).

### Purpose:
- To provide a dedicated `settings.py` configuration for Docker-based deployments.
- To ensure compatibility with containerized services, such as database connections, static file handling,
  or any Docker-specific environment variables.

### Usage:
Set the environment variable `DJANGO_SETTINGS_MODULE` to `conduit.settings_container`
   when running the Django application inside a Docker container.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

from .settings import *
import os

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'change_me')

DEBUG = os.getenv('DJANGO_DEBUG', 'False') == 'True'

# Ensure the directory for the SQLite database exists.
# We pack the db into a folder to easily mount a docker volume.
db_dir = os.path.join(BASE_DIR, 'db')
if not os.path.exists(db_dir):
    os.makedirs(db_dir)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(db_dir, 'db.sqlite3'),
    }
}

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '').split(',')
CORS_ORIGIN_WHITELIST = tuple(os.getenv('CORS_ORIGIN_WHITELIST', 'http://localhost:4000,http://127.0.0.1:4000').split(','))
