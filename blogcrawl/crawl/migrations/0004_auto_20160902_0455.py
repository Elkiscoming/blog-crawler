# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-02 04:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawl', '0003_auto_20160901_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='in_degree',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='name',
            field=models.CharField(max_length=60, unique=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='out_degree',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
