# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, HiddenInput


# Create your models here.


class Point(models.Model):
    title = models.CharField(max_length=100)
    street = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    lat = models.CharField(max_length=100, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    visited = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)

    def color(self):
        if self.visited:
            return "greenIcon"
        else:
            return "redIcon"

    def __unicode__(self):
        return u'%s, %s' % (self.title, self.street)

# nearly working ModelForm
# cant quite figure out why the form is not valid
# and how to save the owner
class PointFormTest(ModelForm):
    class Meta:
        model = Point
        fields = ['title', 'street', 'city', 'lat', 'lng', 'visited']
        widgets = {
            'title': TextInput(attrs={'placeholder': 'Mein Ziel'}),
            'street': TextInput(attrs={'placeholder': 'gewuenschte Straße'}),
            'city': TextInput(attrs={'placeholder': 'gewuenschte Stadt'}),
            'lat': HiddenInput(),
            'lng': HiddenInput(),
        }
        labels = {
            'title': 'Titel',
            'street': 'Straße',
            'city': 'Stadt',
            'visited': 'Besucht?'
        }