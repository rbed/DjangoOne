# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-16 05:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0005_auto_20170810_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='when',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 16, 5, 31, 5, 931589, tzinfo=utc)),
        ),
    ]