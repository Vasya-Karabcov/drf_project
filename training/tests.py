from django.test import TestCase
import pytest
from rest_framework import status
from django.urls import reverse
from training.models import Lesson, Subscription
from training.serliazers import LessonSerializer


@pytest.mark.django_db
class TestLessonViews:

    def test_list_lessons(self, client, user, lesson):
        url = reverse('course:lesson-list')
        client.force_authenticate(user=user)
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_create_lesson(self, client, super_user, course):
        url = reverse('course:lesson_create')
        client.force_authenticate(user=super_user)
        data = {
            'title': 'New Lesson',
            'description': 'New Lesson Description',
            'course': course.id,
            'url': 'https://www.youtube.com/testlesson'
        }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Lesson.objects.filter(title='New Lesson').exists()

    def test_retrieve_lesson(self, client, user, lesson):
        url = reverse('course:lesson_detail', kwargs={'pk': lesson.id})
        client.force_authenticate(user=user)
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert LessonSerializer(lesson).data == response.data

    def test_update_lesson(self, client, user, lesson):
        url = reverse('course:lesson_update', kwargs={'pk': lesson.id})
        client.force_authenticate(user=user)
        data = {'title': 'Updated Lesson'}
        response = client.patch(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert Lesson.objects.get(id=lesson.id).title == 'Updated Lesson'

    def test_delete_lesson(self, client, super_user, lesson):
        url = reverse('course:lesson_delete', kwargs={'pk': lesson.id})
        client.force_authenticate(user=super_user)
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Lesson.objects.filter(id=lesson.id).exists()



@pytest.mark.django_db
class TestSubscriptionViews:

    def test_subscribe_course(self, client, user, course):
        url = reverse('course:subscribe_course', kwargs={'course_id': course.id})
        client.force_authenticate(user=user)
        response = client.post(url)
        assert response.status_code == status.HTTP_201_CREATED
        assert Subscription.objects.filter(user=user, course=course).exists()

    def test_unsubscribe_course(self, client, user, subscription):
        url = reverse('course:unsubscribe_course', kwargs={'course_id': subscription.course.id})
        client.force_authenticate(user=user)
        response = client.delete(url)
        assert response.status_code == status.HTTP_200_OK
        assert not Subscription.objects.filter(id=subscription.id).exists()