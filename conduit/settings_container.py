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