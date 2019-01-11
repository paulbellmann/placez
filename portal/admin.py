# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Point

# Register your models here.
class PointAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'street', 'owner')

# Register your models here.
admin.site.register(Point, PointAdmin)