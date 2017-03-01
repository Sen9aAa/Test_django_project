from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class RequestHistoryView(TemplateView):
	template_name = 'request_history.html'
