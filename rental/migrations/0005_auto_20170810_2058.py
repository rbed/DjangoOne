# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-10 18:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0004_rental_when'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='when',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 10, 18, 58, 9, 95017, tzinfo=utc)),
        ),
    ]
