from rest_framework import serializers

from training.models import Courses, Lesson, Pay, Subscription
from training.services import get_stripe_session
from training.validators import validator_scam_url


class LessonSerializer(serializers.ModelSerializer):
    url = serializers.URLField(validators=[validator_scam_url])
    """Сериализатор модели урока """

    class Meta:
        model = Lesson
        fields = '__all__'


class CoursesSerializer(serializers.ModelSerializer):
    """Сериализатор модели курса """

    lesson_count = serializers.SerializerMethodField()
    lesson = LessonSerializer(many=True, read_only=True, source='lesson_set')
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Courses
        fields = '__all__'

    def get_lesson_count(self, obj):
        """Возвращает кол. уроков в курсе"""
        return obj.lesson_set.count()

    def get_is_subscribed(self, obj):
        """
            Возвращает информацию о том, подписан ли пользователь на обновления курса.
        """
        user = self.context['request'].user

        return Subscription.objects.filter(user=user, course=obj).exists()


class PaySerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Pay
        fields = '__all__'

    def get_url(self, obj: Pay):
        session = get_stripe_session(obj.session)
        return session.url


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
