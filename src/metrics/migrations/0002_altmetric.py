# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 15:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('identifiers', '0002_auto_20170711_1203'),
        ('metrics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AltMetric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(choices=[('twitter', 'Twitter'), ('crossref', 'Crossref'), ('datacite', 'DataCite'), ('reddit', 'Reddit'), ('reddit-links', 'Reddit Links'), ('hypothesis', 'Hypothesis'), ('newsfeed', 'News'), ('stackexchange', 'Stack Exchange'), ('web', 'Web'), ('wikipedia', 'Wikipedia'), ('wordpressdotcom', 'Wordpress')], max_length=30)),
                ('pid', models.TextField()),
                ('timestamp', models.DateTimeField()),
                ('identifier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='identifiers.Identifier')),
            ],
        ),
    ]