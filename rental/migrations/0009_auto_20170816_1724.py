# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-16 15:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0008_auto_20170816_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='when',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 16, 15, 24, 38, 783453, tzinfo=utc)),
        ),
    ]
