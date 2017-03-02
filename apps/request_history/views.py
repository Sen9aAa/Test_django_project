from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import RequestHistory
from django.db.models import F

# Create your views here.
class RequestHistoryView(TemplateView):
    
    template_name = 'request_history.html'

    def get_context_data(self,**kwargs):
        context = super(RequestHistoryView,self).get_context_data(**kwargs)
        request_history_object = RequestHistory.objects.order_by('-request_time')
        for c in request_history_object:
            if c.request_status == 0:
                c.request_status = F('request_status')+1
                c.save(update_fields=['request_status'])        
        context['request_history_objects'] = request_history_object
        return context
    