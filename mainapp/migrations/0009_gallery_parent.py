# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-25 17:42
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='mainapp.Gallery'),
        ),
    ]
