# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-10 18:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0002_auto_20170810_2050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rental',
            name='returned',
        ),
        migrations.RemoveField(
            model_name='rental',
            name='when',
        ),
    ]
