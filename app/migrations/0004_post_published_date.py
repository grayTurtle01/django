# Generated by Django 2.2.12 on 2020-04-18 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200418_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
