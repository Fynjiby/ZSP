# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 17:22
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0003_auto_20170616_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupservices',
            name='text',
            field=tinymce.models.HTMLField(default=1),
            preserve_default=False,
        ),
    ]