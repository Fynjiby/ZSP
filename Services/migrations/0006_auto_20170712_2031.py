# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-12 17:31
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0005_auto_20170619_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupservices',
            name='text',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]
