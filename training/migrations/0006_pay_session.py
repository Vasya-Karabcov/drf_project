# Generated by Django 4.2.5 on 2024-01-09 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0005_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='pay',
            name='session',
            field=models.CharField(blank=True, max_length=350, null=True, unique=True, verbose_name='текущая сессия для оплаты'),
        ),
    ]
