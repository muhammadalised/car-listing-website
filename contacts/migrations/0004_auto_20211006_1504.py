# Generated by Django 3.0.7 on 2021-10-06 10:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20211006_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='create_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
