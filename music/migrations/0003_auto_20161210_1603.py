# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-10 08:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_is_favorite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='is_favorite',
            new_name='Favorite',
        ),
    ]
