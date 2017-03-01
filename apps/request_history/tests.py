from django.test import TestCase,Client
from django.core.urlresolvers import resolve,reverse
from mock import Mock
from .my_middleware import RequestHistoryMiddleware
from .models import RequestHistory
# Create your tests here.


class Request_test(TestCase):
    def setUp(self):
        self.client = Client()
        self.middleware = RequestHistoryMiddleware()
        self.request = Mock()
        self.request.META = {
                            'REQUEST_METHOD' : 'POST',
                            'HTTP_USER_AGENT' : 'AUTOMATED TEST',
                            'HTTP_REFERER' : 'http://127.0.0.1:8000/request_history'
                            }
    
    def test_request_middleware(self):
        response = self.middleware.process_request(self.request)
        self.assertTrue(response == None)
    
    def test_request_model(self):
        instance = RequestHistory.objects.create(request_method = 'POST',
                                                request_link = 'http://127.0.0.1:8000/request_history')
        self.assertTrue(isinstance(instance, RequestHistory))
        self.assertEqual(RequestHistory.objects.all().count(),1)
    
    def test_request_middleware_stors_requests(self):
        for c in range(2):
            url = reverse("home")
            response = self.client.get(url)
        response = self.client.post(url)
        self.assertEqual(RequestHistory.objects.all().count(),3)
    
    def test_request_to_store_only_10_request_to_database(self):
        for c in range(15):
            url = reverse("home")
            response = self.client.get(url)
        self.assertEqual(RequestHistory.objects.all().count(),10)
    def test_request_url(self):
        found = resolve('/request_history')
        self.assertEqual(found.func.__name__,'RequestHistoryView')