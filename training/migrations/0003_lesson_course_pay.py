# Generated by Django 5.0 on 2023-12-17 00:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0002_rename_name_courses_title_rename_name_lesson_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='training.courses', verbose_name='Курс'),
        ),
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=250, verbose_name='Пользователь')),
                ('date_pay', models.DateTimeField(blank=True, null=True, verbose_name='Дата оплаты')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='сумма оплаты')),
                ('pay_method', models.CharField(choices=[('cash', 'Наличные'), ('transfer', 'Перевод на счет')], default='cash', max_length=10, verbose_name='способ оплаты')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='training.courses', verbose_name='оплаченный курс')),
                ('lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='training.lesson', verbose_name='оплаченный урок')),
            ],
        ),
    ]
