# Generated by Django 3.0.7 on 2021-10-06 10:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_auto_20211006_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 6, 15, 4, 2, 472120)),
        ),
    ]
