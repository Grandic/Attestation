from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='d.bitkoff@yandex.ru',
            first_name='Dmitry',
            last_name='Bitkov',
            is_superuser=True,
            is_staff=False,
            is_active=True
        )

        user.set_password('151087')
        user.save()
