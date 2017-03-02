from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import MyInfo
from apps.request_history.models import RequestHistory


# Create your views here.
class HomeView(TemplateView):
    
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super(HomeView,self).get_context_data(**kwargs)
        my_instanse = MyInfo.objects.all()
        requests_instanse = RequestHistory.objects.all()
        requests_number = 0
        for c in requests_instanse:
            if c.request_status == 0:
                requests_number+=1
        context['my_instanse'] = my_instanse
        context['requests_number'] = requests_number
        return context    


    