# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-14 20:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trackMusic', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Genere',
            new_name='Genre',
        ),
        migrations.RenameModel(
            old_name='TrackGenereMap',
            new_name='TrackGenreMap',
        ),
        migrations.RenameField(
            model_name='genre',
            old_name='genere_name',
            new_name='genre_name',
        ),
        migrations.RenameField(
            model_name='trackgenremap',
            old_name='genere_id',
            new_name='genre_id',
        ),
        migrations.AlterUniqueTogether(
            name='trackgenremap',
            unique_together=set([('track_id', 'genre_id')]),
        ),
    ]