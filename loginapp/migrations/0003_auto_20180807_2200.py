# Generated by Django 2.1 on 2018-08-07 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0002_auto_20180807_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackedemail',
            name='passchar',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='hackedemail',
            name='user_email',
            field=models.CharField(max_length=400),
        ),
    ]
