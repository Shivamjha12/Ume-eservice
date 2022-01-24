from django.contrib import admin
from django.urls import path, include
from ume import views 


urlpatterns = [
    path('', views.dashboard, name='dhashboard'),
    path('accounts/', include('accounts.urls')),
    path('addjob', views.addjob, name='addjob'),
    path('jobslist', views.userjoblist, name='jobslist'),
    
]
 