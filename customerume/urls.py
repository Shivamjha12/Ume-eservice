from django.contrib import admin
from django.urls import path, include
from customerume import views 


urlpatterns = [
    path('', views.index, name='index'),
    path('categories',views.cat,name='categories'),
    path('profile',views.profile,name='profile')
    
]
 