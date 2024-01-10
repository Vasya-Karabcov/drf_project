import os

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from training.models import Subscription, Courses

@shared_task
def sending_emails_about_updates(course_pk):
    subscriptions = Subscription.objects.filter(course=course_pk)
    course = Courses.objects.get(pk=course_pk)
    for subscription in subscriptions:
        send_mail(
            subject=f'Обновление курса {course}',
            message='В курсе появились новые материалы',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[subscription.user.email],
            fail_silently=False
        )