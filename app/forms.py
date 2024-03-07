from django import forms 
from .models import *
from .resources import *
from django.contrib.auth.models import User



class DateInput(forms.DateInput):
    input_type = 'date'
        


class loginform(forms.Form):
    username = forms.CharField(max_length=30, label='',widget=forms.TextInput (attrs={'placeholder': 'username'}))
    password = forms.CharField(label=(""), widget=forms.PasswordInput (attrs={'placeholder': 'password'}))
    def clean(self):
        cleaned_data = super(loginform, self).clean()
        return cleaned_data 


mar_status = (('married', 'married'),('single', 'single'),('divorce','divorce'), ('widow(er)','widow(er)'))

class Memberform(forms.Form):
    name = forms.CharField(label='', widget=forms.TextInput (attrs={'placeholder': 'Name'}))
    contact = forms.CharField(label='', widget=forms.TextInput (attrs={'placeholder': 'Contact'}))
    profession = forms.CharField(label='', widget=forms.TextInput (attrs={'placeholder': 'profession'}))
    residence = forms.CharField(label='', widget=forms.TextInput (attrs={'placeholder': 'residence'}))
    mstatus = forms.CharField(choices=mar_status, default='married', max_length=10)
    def clean(self):
        cleaned_data = super(Memberform, self).clean()
        return cleaned_data 








