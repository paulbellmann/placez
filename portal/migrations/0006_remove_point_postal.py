# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-14 14:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_auto_20180414_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='point',
            name='postal',
        ),
    ]
