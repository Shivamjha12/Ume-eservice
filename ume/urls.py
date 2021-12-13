from django.contrib import admin
from django.urls import path, include
from ume import views 


urlpatterns = [
    path('home', views.home, name='home'),
    path('addjob', views.addjob, name='addjob'),
    path('jobs', views.jobs, name='addjob')
]
 