# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-14 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_remove_point_postal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='lat',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='point',
            name='lng',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
