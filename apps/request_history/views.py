from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import RequestHistory

# Create your views here.
class RequestHistoryView(TemplateView):
    template_name = 'request_history.html'

    def get_context_data(self,**kwargs):
        context = super(RequestHistoryView,self).get_context_data(**kwargs)
        request_history_object = RequestHistory.objects.order_by('-request_time')
        context['request_history_objects'] = request_history_object
        return context
    