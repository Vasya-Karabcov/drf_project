import django_filters
from .models import Pay


class PayFilter(django_filters.FilterSet):
    ordering = django_filters.OrderingFilter(
        fields=(
            ('date', 'date'),

        ),
        field_labels={
            'date': 'Дата',
        },
        label='Сортировать'
    )

    class Meta:
        model = Pay
        fields = ['course', 'lesson', 'pay_method']
