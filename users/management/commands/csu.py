from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='test@mail.ru',
            first_name='Test',
            last_name='Testov',
            is_superuser=True,
            is_staff=False,
            is_active=True
        )

        user.set_password('658311')
        user.save()
