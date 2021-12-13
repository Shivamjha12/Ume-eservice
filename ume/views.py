from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from ume.forms import ServiceProviderPost
from accounts.models import CustomUser
# Create your views here.
def home(request):
    return render(request,'ume/home.html')

def addjob(request): 
    if request.method == 'GET':
        try:
            user = request.user
            print(user)
            seller=user.type
            print(seller)
            if user.type == seller:
                print("Working seller condition XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            # if request.user == CustomUser.type.SELLER:
                # form         = ServiceProviderPost(request.POST)
                # addjob      = form.save(commit=False)
                # addjob.user = request.user
                # addjob.save()
                # return redirect('home')
            elif user.type != seller:
                print("working else condition QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ")
                # redirect('accounts/seller.register')

        except ValueError:
            return render(request, 'home.html',{'error':'Bad data request'} )
def jobs(request):
    if request.method == 'POST':
        return render(request, 'ume/jobs.html')

    # template_name = 'addjob.html'
    # success_url = '/home'
    # form_class = ServiceProviderPost
    