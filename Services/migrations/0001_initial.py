# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 19:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroupServices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('icone', models.ImageField(upload_to=b'img/')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('min_text', tinymce.models.HTMLField()),
                ('max_text', tinymce.models.HTMLField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Services.GroupServices')),
            ],
        ),
    ]
