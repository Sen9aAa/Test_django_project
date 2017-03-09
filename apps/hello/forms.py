from django import forms
from .models import MyInfo
from apps.hello.widgets.Date_widget import DateWidget


class My_add_data_form(forms.ModelForm):
    class Meta:
        model = MyInfo
        fields = '__all__'
        widgets={'birthday':DateWidget(usel10n=True, bootstrap_version=3)}        
        