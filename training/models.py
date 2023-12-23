from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Courses(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название курса')
    image = models.ImageField(upload_to='сourses/', verbose_name='Превью', **NULLABLE)
    description = models.CharField(max_length=550, verbose_name='Описание')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название урока')
    description = models.CharField(max_length=550, verbose_name='Описание')
    image = models.ImageField(upload_to='lesson/', verbose_name='Превью', **NULLABLE)
    link = models.CharField(max_length=350, verbose_name='Ссылка на видео')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    course = models.ForeignKey(Courses, on_delete=models.CASCADE, verbose_name="Курс", **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Pay(models.Model):
    user = models.CharField(max_length=250, verbose_name='Пользователь')
    date_pay = models.DateTimeField(verbose_name='Дата оплаты', **NULLABLE)
    course = models.ForeignKey('Courses', on_delete=models.CASCADE, null=True, blank=True,
                               verbose_name="оплаченный курс")
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE, null=True, blank=True,
                               verbose_name="оплаченный урок")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="сумма оплаты")

    PAY_METHOD_CHOICES = [('cash', 'Наличные'), ('transfer', 'Перевод на счет'), ]
    pay_method = models.CharField(max_length=10, choices=PAY_METHOD_CHOICES, default='cash',
                                  verbose_name='способ оплаты')

    def __str__(self):
        return f'{self.user.email} - {self.date_pay} - {self.amount}'
