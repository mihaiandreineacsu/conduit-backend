import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Create a superuser if the environment variables are set'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        email = os.getenv('DJANGO_SUPERUSER_EMAIL')
        username = os.getenv('DJANGO_SUPERUSER_USERNAME')
        password = os.getenv('DJANGO_SUPERUSER_PASSWORD')

        if not (email and username and password):
            self.stdout.write(self.style.ERROR('Environment variables for superuser creation are not set.'))
            return

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f'Superuser "{username}" already exists.'))
            return

        User.objects.create_superuser(username=username, email=email, password=password)
        self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" created successfully.'))
