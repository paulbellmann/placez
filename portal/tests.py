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
        self.point = Point.objects.create(title='Wien', visited=True, owner=self.user)

    def test_correct_title(self):
        wien = Point.objects.get(title='Wien')
        self.assertEqual(wien.title, 'Wien')


class HomeTest(TestCase):
    """point creating / retrieving multiple"""

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.pointA = Point.objects.create(title='Zu hauße', visited=True, owner=self.user)
        self.pointB = Point.objects.create(title='Sühlen', visited=False, owner=self.user)

    def test_home_displays_data(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Zu hauße')
        self.assertContains(response, 'Sühlen')
        self.assertNotContains(response, 'Try adding new Places with')
        self.assertContains(response, 'visited')
        self.assertContains(response, 'wanted')
        self.assertEqual(len(response.context['items']), 2)


class NewUserTest(TestCase):
    """Creating Acc and loggin in, testing messages"""

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_message_after_registration(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        m = list(response.context['messages'])
        self.assertEqual(len(m), 1)
        self.assertEqual(str(m[0]), "Try adding new places with 'Add new'")


class NotLoggedInTest(TestCase):
    """Trying to access home with no acc / redirect"""

    def test_not_logged_in(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)


class DeleteTest(TestCase):
    """deleting a point"""

    def setUp(self):
        self.userA = User.objects.create_user(username='testuserA', password='12345')
        self.client.login(username='testuserA', password='12345')
        self.pointA = Point.objects.create(title='Ehksaal', visited=True, owner=self.userA)
        self.client.logout()

        self.userB = User.objects.create_user(username='testuserB', password='12345')
        self.client.login(username='testuserB', password='12345')
        self.pointB = Point.objects.create(title='Sühlen', visited=True, owner=self.userB)
        self.client.logout()

    def test_deleting_own(self):
        self.client.login(username='testuserA', password='12345')
        response = self.client.get('/delete/1', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/portal/')
        self.assertEqual(Point.objects.all().count(), 1) # 1 because we created 2
        self.assertFalse(Point.objects.all().filter(pk=self.pointA.id).exists())
        m = list(response.context['messages'])
        self.assertEqual(len(m), 2) # 2 because index() adds another message
        self.assertEqual(str(m[0]), "Ehksaal got deleted.")

    def test_deleting_not_own(self):
        self.client.login(username='testuserB', password='12345')
        response = self.client.get('/delete/1')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Point.objects.all().count(), 2)
        self.assertTrue(Point.objects.all().filter(pk=self.pointA.id).exists())


class ShowAllTest(TestCase):
    """showing all points in a big map"""

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.pointA = Point.objects.create(title='Monaco', visited=True, owner=self.user)
        self.pointB = Point.objects.create(title='Marbella', visited=False, owner=self.user)

    def test_show_all_map(self):
        response = self.client.get('/show_all')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Monaco')
        self.assertContains(response, 'Marbella')
        self.assertEqual(len(response.context['items']), 2)


class EditPointTest(TestCase):
    """Editing a point and saving it"""

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.point = Point.objects.create(title='Monaco', visited=True, owner=self.user)

    def test_editing_point_post(self):
        response = self.client.post('/edit_point/1', {'title': 'Hamburg', 'city': 'Hamburg', 'visited': '1'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Point.objects.get(id=1).title, 'Hamburg')
        self.assertEqual(Point.objects.get(id=1).city, 'Hamburg')

    def test_editing_point_get(self):
        response = self.client.get('/edit_point/1')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Monaco')
        self.assertEqual(response.context['item'], self.point)



class AddPointTest(TestCase):
    """Creating Acc, login, point creating a point"""

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_adding_point_post(self):
        response = self.client.post('/add_new', {'title': 'Arbeit', 'city': 'Lübeck', 'visited': '1'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/portal/')
        m = response.context['messages']
        m = list(response.context['messages'])
        self.assertEqual(len(m), 1)
        self.assertEqual(str(m[0]), "Arbeit got saved.")
        self.assertTrue("Arbeit got" in str(m[0]))
        self.assertEqual(Point.objects.get(id=1).title, 'Arbeit')

    def test_adding_point_get(self):
        response = self.client.get('/add_new')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Add new')