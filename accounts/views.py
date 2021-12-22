from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.views.generic import View
from django.contrib.auth import authenticate,login,logout
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
    
# class Login(LoginView):
#     template_name = 'login.html'
#     success_url ='/home'
    
class Login(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return redirect('/home')
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)

        return render(request, "index.html")

def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('user_login')
    return redirect('home')
    
class sellerregistrationform(LoginRequiredMixin,CreateView):
    template_name = 'registration_seller.html'
    success_url = reverse_lazy('user_login')
    form_class = sellerSignupForm
    
    def form_valid(self, form):
        user = self.request.user
        user.type.append(user.Types.SELLER)
        user.save()
        form.instance.user = self.request.user
        return super().form_valid(form)

    