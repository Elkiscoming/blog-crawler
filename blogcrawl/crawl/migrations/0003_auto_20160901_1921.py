# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-01 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawl', '0002_auto_20160727_0847'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='in_degree',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='out_degree',
            field=models.IntegerField(null=True),
        ),
    ]
