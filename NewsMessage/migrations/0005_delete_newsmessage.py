# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 21:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NewsMessage', '0004_newsmessage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NewsMessage',
        ),
    ]
