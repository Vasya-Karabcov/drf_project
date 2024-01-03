from rest_framework import serializers

from training.models import Courses, Lesson, Pay, Subscription


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор модели урока """

    class Meta:
        model = Lesson
        fields = '__all__'


class CoursesSerializer(serializers.ModelSerializer):
    """Сериализатор модели курса """

    lesson_count = serializers.SerializerMethodField()
    lesson = LessonSerializer(many=True, read_only=True, source='lesson_set')

    class Meta:
        model = Courses
        fields = '__all__'

    def get_lesson_count(self, obj):
        """Возвращает кол. уроков в курсе"""
        return obj.lesson_set.count()


class PaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pay
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    """
       Сериализатор для модели подписки на курс.
       Attributes:
           model (Subscription): Модель, которая используется для сериализации.
           fields : Поля, которые будут сериализованы (все поля).
    """

    class Meta:
        model = Subscription
        fields = '__all__'
