# Generated by Django 2.2.12 on 2021-10-13 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='image',
        ),
        migrations.RemoveField(
            model_name='info',
            name='user',
        ),
    ]
