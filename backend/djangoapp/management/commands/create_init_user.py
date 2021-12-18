from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError


def create_super_user():
    try:
        User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    except IntegrityError:
        pass


class Command(BaseCommand):
    help = 'Create first admin super user'

    def handle(self, *args, **options):
        create_super_user()