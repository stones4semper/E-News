# Generated by Django 2.1.7 on 2019-03-27 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190327_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='CatName',
            field=models.CharField(max_length=100),
        ),
    ]
