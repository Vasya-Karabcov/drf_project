import pytest
from rest_framework.test import APIClient

from training.models import Courses, Lesson, Subscription
from users.models import User


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def user():
    return User.objects.create(email='testuser@example.com',
                               password='testpassword', role='moderator')


@pytest.fixture
def super_user():
    super_user = User.objects.create(
        email='testadmin@example.com',
        password='testpassword',
        first_name='Admin',
        last_name='LMS',
        is_staff=True,
        is_superuser=True
    )
    return super_user


@pytest.fixture
def course():
    return Courses.objects.create(title='Test Course', description='Test Description')


@pytest.fixture
def lesson(course):
    return Lesson.objects.create(title='Test Lesson', description='Test Lesson Description', course=course)


@pytest.fixture
def subscription(user, course):
    return Subscription.objects.create(user=user, course=course)