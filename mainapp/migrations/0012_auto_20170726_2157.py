# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-26 18:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_gallery_image_small'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery',
            old_name='unit',
            new_name='Unit',
        ),
    ]
