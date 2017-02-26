from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import resolve,reverse
from django.http import HttpRequest
from .views import HomeView
# Create your tests here.


class SomeTests(TestCase):
    def setUp(self):
        self.client = Client()
    def test_math(self):
        "put docstrings in your tests"
        assert(2 + 3 == 5)
    def test_hello_url(self):
        found = resolve('/')
        self.assertEqual(found.func.__name__,'HomeView')
    def test_view_too_return_content(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertIn(b'<title>42 cofee cups</title>', response.content)
