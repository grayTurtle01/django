# Generated by Django 2.2.12 on 2020-04-18 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(default='defaul text'),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='default title', max_length=200),
        ),
    ]
