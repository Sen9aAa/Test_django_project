from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import MyInfo

# Create your views here.
class HomeView(TemplateView):
    
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super(HomeView,self).get_context_data(**kwargs)
        my_instanse = MyInfo.objects.all()
        context['my_instanse'] = my_instanse
        return context    


    