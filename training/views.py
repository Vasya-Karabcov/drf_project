from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics

from training.filters import PayFilter
from training.models import Courses, Lesson, Pay
from training.permissions import IsOwner, IsModerator
from training.serliazers import CoursesSerializer, LessonSerializer, PaySerializer

from rest_framework.permissions import IsAuthenticated, IsAdminUser


class CoursesViewSet(viewsets.ModelViewSet):
    serializer_class = CoursesSerializer
    queryset = Courses.objects.prefetch_related('lesson_set').all()

    def get_permissions(self):
        """Права доступа"""
        if self.action == 'retrieve':
            permission_classes = {IsOwner | IsModerator | IsAdminUser}
        elif self.action == 'create':
            permission_classes = [IsAdminUser]
        elif self.action == 'destroy':
            permission_classes = [IsOwner | IsAdminUser]
        elif self.action == 'update':
            permission_classes = [IsOwner | IsModerator | IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = {IsAdminUser}


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = {IsOwner | IsModerator | IsAdminUser}


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = {IsOwner | IsModerator | IsAdminUser}


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = {IsOwner | IsAdminUser}


class PayViewSet(viewsets.ModelViewSet):
    queryset = Pay.objects.all()
    serializer_class = PaySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PayFilter
