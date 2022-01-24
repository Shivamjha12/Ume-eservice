from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from ume.forms import ServiceProviderPost
from accounts.models import CustomUser
from ume.models import sellerPost
from accounts.urls import *
# Create your views here.

def addjob(request): 
    user = request.user
    userType=user.type
    # if str(userType) == "SELLER":
    if request.method=="POST":
        form         = ServiceProviderPost(request.POST)
        addjob      = form.save(commit=False)
        addjob.user = user
        addjob.save()
        return redirect('/')
    elif str(userType) == "CUSTOMER":
        return redirect('form_seller')
    return render(request, 'ume/jobs.html',{'form':ServiceProviderPost()})
def userjoblist(request):
    user=request.user
    joblist = sellerPost.objects.filter(user=user)
    return render(request, 'ume/userjoblist.html',{'joblist':joblist})
def dashboard(request):
    return render(request, 'ume/dhasboard.html')
    # template_name = 'addjob.html'
    # success_url = '/home'
    # form_class = ServiceProviderPost
    