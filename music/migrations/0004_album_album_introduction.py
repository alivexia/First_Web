# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-13 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20161210_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_introduction',
            field=models.CharField(default='SOME STRING', max_length=10240),
        ),
    ]