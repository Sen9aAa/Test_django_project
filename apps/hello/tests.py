from django.test import TestCase,Client
from django.core.urlresolvers import resolve,reverse
from django.http import HttpRequest
from .views import HomeView
from .models import MyInfo
from datetime import date
from django.contrib.auth.models import User
from apps.request_history.models import RequestHistory
# Create your tests here.


class SomeTests(TestCase):
    fixtures = ['initial_data.json']  

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
        self.assertIn('<title>42 cofee cups</title>', response.content)
    
    def test_model_MyInfo(self):
        instance = MyInfo.objects.create(name = 'Test',
                                        surname = 'Testovuch',
                                        email = 'test1990@gmail.com',
                                        bio = 'live in Lviv',
                                        birthday = date(1990,02,21)
                                        )
        self.assertTrue(isinstance(instance, MyInfo))
        self.assertEqual(instance.name,'Test')

    def test_fixture(self):
        fixtures_instant_name = MyInfo.objects.get(pk = 1).name
        self.assertEqual(MyInfo.objects.count(),1)
        self.assertEqual(fixtures_instant_name,'Oleg')

    def test_fixture_superuser(self):
        user_instanc = User.objects.get(id = 1)
        self.assertTrue(user_instanc.is_superuser)
        self.assertEqual(user_instanc.username,'admin')    
    
    def test_view_use_model(self):
        response = self.client.get('/')
        model_instance = MyInfo.objects.get(pk =1)
        self.assertIn(model_instance.name,response.content)
        self.assertIn(model_instance.surname,response.content)

        

        
 
