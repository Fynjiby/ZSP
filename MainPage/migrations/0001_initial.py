# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 16:06
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_text', models.CharField(max_length=500)),
                ('main_text', tinymce.models.HTMLField()),
            ],
        ),
    ]
