# Generated by Django 2.1.1 on 2018-10-24 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_auto_20181023_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='time',
        ),
        migrations.AddField(
            model_name='location',
            name='time',
            field=models.IntegerField(default=0),
        ),
    ]
