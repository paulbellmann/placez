# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-15 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0010_point_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
