# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-01-07 19:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0011_auto_20180415_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='street',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
