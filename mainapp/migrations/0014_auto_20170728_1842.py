# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-28 15:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_auto_20170728_1841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='parent',
        ),
        migrations.DeleteModel(
            name='Unit',
        ),
    ]
