from django.test import TestCase,Client
from django.core.urlresolvers import resolve,reverse
from django.http import HttpRequest
from .views import HomeView
from .models import MyInfo
from datetime import date
from django.contrib.auth.models import User
from apps.request_history.models import RequestHistory
from .forms import *
import tempfile
from django.core.files.images import ImageFile
# Create your tests here.


class SomeTests(TestCase):
    fixtures = ['initial_data.json']

    def get_test_image_file(self):
        file = tempfile.NamedTemporaryFile(suffix='.png')
        return ImageFile(file, name=file.name)  

    def setUp(self):
        self.client = Client()
        self.data = {'name' : 'Test','surname' : 'Testovuch','email' : 'test1990@gmail.com','bio' : 'live in Lviv','birthday' : date(1990,02,21)}
    
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
        
    def test_form_add_data_is_valid(self):
        form = My_add_data_form(data = self.data)
        self.assertTrue(form.is_valid())
        instance = form.save()
        self.assertEqual(instance.name,'Test')
    
    def test_form_is_not_valid(self):
        form = My_add_data_form(data = {})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'] and form.errors['surname'] and form.errors['email'] and form.errors['birthday'],['This field is required.'])

    def test_form_using_teamplate(self):
        response = self.client.get('/add_data')
        self.assertTemplateUsed(response, 'add_data.html')
        self.assertIsInstance(response.context['form'], My_add_data_form)

    def test_form_save_data_to_bd(self):
        response = self.client.post('/add_data',self.data)
        instance = MyInfo.objects.get(id = 2)
        self.assertEqual(MyInfo.objects.all().count(),2)
        self.assertEqual(instance.name,'Test')
    
    def test_the_image_field_in_MyInfo(self):
        instance = MyInfo.objects.create(name = 'Test',
                                        surname = 'Testovuch',
                                        email = 'test1990@gmail.com',
                                        bio = 'live in Lviv',
                                        birthday = date(1990,02,21),
                                        image = self.get_test_image_file(),
                                        )
        file = instance.image.path
        self.assertTrue(isinstance(instance, MyInfo))
        self.failUnless(open(file), 'file not found')

    def test_form_add_data_is_valid_whith_image_field(self):
        self.data['image'] = self.get_test_image_file()
        form = My_add_data_form(data = self.data)
        self.assertTrue(form.is_valid())
        instance = form.save()
        self.assertEqual(instance.name,'Test')


        
 
