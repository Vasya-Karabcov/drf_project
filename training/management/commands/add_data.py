import os

from django.conf import settings
from django.core.management.base import BaseCommand

from training.services import create_stripe_session
from users.models import User, UserRoles
from training.models import Courses, Lesson, Pay
from faker import Faker
import random
from decimal import Decimal

fake = Faker()


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        Pay.objects.all().delete()
        Lesson.objects.all().delete()
        Courses.objects.all().delete()
        User.objects.all().delete()

        super_user = User.objects.create(
            email=settings.EMAIL_HOST_USER,
            first_name='Admin',
            last_name='LMS',
            is_staff=True,
            is_superuser=True
        )
        super_user.set_password(os.getenv('ADMIN_PASSWORD'))
        super_user.save()
        moderator_user = User.objects.create(
            email=os.getenv('MODERATOR_EMAIL'),
            first_name='Admin',
            last_name='LMS',
            role=UserRoles.MODERATOR
        )
        moderator_user.set_password(os.getenv('ADMIN_PASSWORD'))
        moderator_user.save()
        users = []
        for _ in range(5):
            email = fake.email()
            phone = fake.numerify()
            country = fake.country()
            first_name = fake.first_name()
            last_name = fake.last_name()
            user = User.objects.create(email=email, phone=phone, country=country,
                                       first_name=first_name, last_name=last_name)
            user.set_password(os.getenv('ADMIN_PASSWORD'))
            user.save()
            users.append(user)

        courses = []
        lessons = []
        for i in range(5):
            course = Courses.objects.create(
                title=fake.word(),
                description=fake.text(),
                owner=users[i],
            )
            courses.append(course)

            for _ in range(3):
                lesson = Lesson.objects.create(
                    title=fake.sentence(),
                    description=fake.text(),
                    course=course,
                    url=fake.url(),
                    owner=users[i],
                )
                lessons.append(lesson)

        for _ in range(20):
            user = random.choice(users)
            payment_date = fake.date_between(start_date='-30d', end_date='today')
            amount = Decimal(random.uniform(10, 100))
            payment_method = random.choice(['cash', 'transfer'])

            is_course = random.choice([True, False])
            course_or_lesson = random.choice(courses) if is_course else random.choice(lessons)
            session = create_stripe_session(course_or_lesson, user, amount)

            Pay.objects.create(
                user=user,
                date=payment_date,
                course=course_or_lesson if is_course else None,
                lesson=course_or_lesson if not is_course else None,
                amount=amount,
                payment_method=payment_method,
                session=session.id
            )