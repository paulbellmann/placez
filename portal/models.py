# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.
class Item(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "%s, %s" % (self.last_name, self.first_name)


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['first_name', 'last_name']


class Point(models.Model):
    title = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    # postal = models.IntegerField()
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    visited = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)
