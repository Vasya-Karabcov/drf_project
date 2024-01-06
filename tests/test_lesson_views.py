import pytest
from django.urls import reverse
from rest_framework import status
from training.models import Lesson
from training.serliazers import LessonSerializer


@pytest.mark.django_db
class TestLessonViews:

    def test_list_lessons(self, client, user, lesson):
        url = reverse('training:lesson_list')
        client.force_authenticate(user=user)
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_create_lesson(self, client, super_user, course):
        url = reverse('training:lesson_create')
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
        url = reverse('training:lesson_get', kwargs={'pk': lesson.id})
        client.force_authenticate(user=user)
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert LessonSerializer(lesson).data == response.data

    def test_update_lesson(self, client, user, lesson):
        url = reverse('training:lesson_update', kwargs={'pk': lesson.id})
        client.force_authenticate(user=user)
        data = {'title': 'Updated Lesson'}
        response = client.patch(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert Lesson.objects.get(id=lesson.id).title == 'Updated Lesson'

    def test_delete_lesson(self, client, super_user, lesson):
        url = reverse('training:lesson_delete', kwargs={'pk': lesson.id})
        client.force_authenticate(user=super_user)
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Lesson.objects.filter(id=lesson.id).exists()