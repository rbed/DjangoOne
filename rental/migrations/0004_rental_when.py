# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-10 18:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0003_auto_20170810_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='rental',
            name='when',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 10, 18, 55, 57, 524450, tzinfo=utc)),
        ),
    ]
