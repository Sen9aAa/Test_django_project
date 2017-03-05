from django import forms
from .models import MyInfo


class My_add_data_form(forms.ModelForm):
    class Meta:
        model = MyInfo
        fields = '__all__'
        