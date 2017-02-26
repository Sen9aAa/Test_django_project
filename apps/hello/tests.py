from django.test import TestCase
from django.core.urlresolvers import resolve
from .views import HomeView
# Create your tests here.


class SomeTests(TestCase):
    def test_math(self):
        "put docstrings in your tests"
        assert(2 + 3 == 5)
    def test_hello_url(self):
        found = resolve('/')
        self.assertEqual(found.func.__name__,'HomeView')

