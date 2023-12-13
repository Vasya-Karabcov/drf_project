from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Courses(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название курса')
    image = models.ImageField(upload_to='сourses/', verbose_name='Превью', **NULLABLE)
    description = models.CharField(max_length=550, verbose_name='Описание')

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

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
