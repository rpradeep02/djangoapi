# Generated by Django 3.1.1 on 2020-09-26 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20200926_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='end_time',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='activity',
            name='start_time',
            field=models.CharField(max_length=30),
        ),
    ]