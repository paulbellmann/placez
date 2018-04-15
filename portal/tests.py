# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from .models import Point
from django.contrib.auth.models import User


# Create your tests here.
class PointTest(TestCase):
    """Creating and retrieving a Point"""

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.point = Point.objects.create(title='Arbeit', visited=True, owner=self.user)

    def test_correct_name(self):
        arbeit = Point.objects.get(title='Arbeit')
        self.assertEqual(arbeit.title, 'Arbeit')


class HomeTest(TestCase):
    """Creating Acc, login, point creating / retrieving multiple"""

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.pointA = Point.objects.create(title='Zu hauße', visited=True, owner=self.user)
        self.pointB = Point.objects.create(title='Sühlen', visited=False, owner=self.user)

    def test_home_returns_correct_html(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Zu hauße')
        self.assertContains(response, 'Sühlen')
        self.assertContains(response, 'visited')
        self.assertContains(response, 'wanted')
        self.assertEqual(len(response.context['items']), 2)


class DetailViewTest(TestCase):
    """Creating Acc, login, point creating / retrieving single"""

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.point = Point.objects.create(title='Übel', visited=True, owner=self.user)

    def test_list_returns_correct_queryset(self):
        response = self.client.get('/edit_point/1')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Übel')
        self.assertEqual(response.context['item'], self.point)


class DeleteTest(TestCase):
    """Creating Acc, login, point creating / and deleting"""

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.point = Point.objects.create(title='Ehksaal', visited=True, owner=self.user)

    def test_list_returns_correct_queryset(self):
        response = self.client.get('/delete/1')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Point.objects.all().count(), 0)
        self.assertFalse(Point.objects.all().filter(pk=self.point.id).exists())
