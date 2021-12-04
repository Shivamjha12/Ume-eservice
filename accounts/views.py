from django.shortcuts import render
from django.views.generic import CreateView
# ,LoginView
# Create your views here.
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from accounts.forms import *
from django.urls import reverse_lazy, reverse
class UserRegeatration(CreateView):
    template_name ='registration.html'
    form_class = CustomUserCreationForm
    success_url = '/accounts/signup/'
    
# class login(LoginView):
    
    