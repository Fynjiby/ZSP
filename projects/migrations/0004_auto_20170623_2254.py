# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_zone_svgpath'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='text',
            field=models.TextField(max_length=100),
        ),
    ]