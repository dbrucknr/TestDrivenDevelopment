from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from lists.views import home_page

# Create your tests here.
# class SmokeTest(TestCase):
#     def test_bad_math(self):
#         self.assertEqual(1+1, 3)

class HomePageTest(TestCase):

    def test_root_url_resolves_to_homepage(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_homepage_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')