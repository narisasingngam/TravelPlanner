# Generated by Django 2.1.1 on 2018-11-05 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0007_auto_20181105_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planner',
            name='time',
            field=models.CharField(default=0, max_length=30),
        ),
    ]