from django.core.management.base import BaseCommand
from users.models import User
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

        users = []
        for _ in range(5):
            email = fake.email()
            password = fake.password()
            phone = fake.numerify()
            country = fake.country()
            user = User.objects.create(email=email, password=password, phone=phone, country=country)
            users.append(user)

        courses = []
        lessons = []
        for _ in range(5):
            course = Courses.objects.create(
                title=fake.word(),
                description=fake.text(),
            )
            courses.append(course)

            for _ in range(3):
                lesson = Lesson.objects.create(
                    title=fake.sentence(),
                    description=fake.text(),
                    course=course,
                    url=fake.url(),
                )
                lessons.append(lesson)

        for _ in range(20):
            user = random.choice(users)
            date_pay = fake.date_between(start_date='-30d', end_date='today')
            amount = Decimal(random.uniform(10, 100))
            pay_method = random.choice(['cash', 'transfer'])

            is_course = random.choice([True, False])
            course_or_lesson = random.choice(courses) if is_course else random.choice(lessons)

            Pay.objects.create(
                user=user,
                date=date_pay,
                course=course_or_lesson if is_course else None,
                lesson=course_or_lesson if not is_course else None,
                amount=amount,
                payment_method=pay_method,
            )