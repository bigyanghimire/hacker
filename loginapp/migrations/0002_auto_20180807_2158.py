# Generated by Django 2.1 on 2018-08-07 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hackedemail',
            name='company',
        ),
        migrations.RemoveField(
            model_name='hackedemail',
            name='link',
        ),
        migrations.RemoveField(
            model_name='hackedemail',
            name='location',
        ),
        migrations.RemoveField(
            model_name='hackedemail',
            name='posted',
        ),
        migrations.RemoveField(
            model_name='hackedemail',
            name='summary',
        ),
        migrations.RemoveField(
            model_name='hackedemail',
            name='title',
        ),
        migrations.AddField(
            model_name='hackedemail',
            name='passchar',
            field=models.CharField(default='hellos', max_length=400),
        ),
        migrations.AddField(
            model_name='hackedemail',
            name='user_email',
            field=models.CharField(default='@Gma', max_length=400),
        ),
    ]
