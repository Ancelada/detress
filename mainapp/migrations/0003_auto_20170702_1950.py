# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 16:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_unit_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Unit',
            new_name='Mainbar',
        ),
    ]