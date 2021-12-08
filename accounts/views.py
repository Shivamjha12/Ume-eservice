from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
# ,LoginView
# Create your views here.
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from accounts.forms import *
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
class UserRegeatration(CreateView):
    template_name ='registration.html'
    form_class = CustomUserCreationForm
    success_url = '/accounts/signup/'
    
class Login(LoginView):
    template_name = 'login.html'
    
class sellerregistrationform(LoginRequiredMixin,CreateView):
    template_name = 'registration_seller.html'
    success_url = reverse_lazy('form_seller')
    form_class = sellerSignupForm
    
    def form_valid(self, form):
        user = self.request.user
        user.type.append(user.Types.SELLER)
        user.save()
        form.instance.user = self.request.user
        return super().form_valid(form)
    