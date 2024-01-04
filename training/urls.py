from django.urls import path

from training.apps import TrainingConfig
from rest_framework.routers import DefaultRouter

from training.views import CoursesViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, PayViewSet, SubscribeCourseView, UnsubscribeCourseView

app_name = TrainingConfig.name

router = DefaultRouter()
router.register(r'courses', CoursesViewSet, basename='courses'),
router.register(r'pay', PayViewSet, basename='pay')

urlpatterns = [
                  path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
                  path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
                  path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_get'),
                  path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
                  path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),
                  path('subscribe/<int:course_id>/', SubscribeCourseView.as_view(), name='subscribe_course'),
                  path('unsubscribe/<int:course_id>/', UnsubscribeCourseView.as_view(), name='unsubscribe_course'),

              ] + router.urls
