# Generated by Django 2.1.1 on 2018-11-05 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0009_auto_20181105_1050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planner',
            name='time',
        ),
        migrations.AddField(
            model_name='planner',
            name='times',
            field=models.CharField(max_length=30, null=True),
        ),
    ]