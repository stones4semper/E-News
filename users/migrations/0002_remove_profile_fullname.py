# Generated by Django 2.1.7 on 2019-03-24 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='fullName',
        ),
    ]
