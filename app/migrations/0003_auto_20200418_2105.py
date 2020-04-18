# Generated by Django 2.2.12 on 2020-04-18 21:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200418_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
