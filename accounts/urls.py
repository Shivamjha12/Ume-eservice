"""
devproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from accounts import views 


urlpatterns = [
    path('signup/', views.UserRegeatration.as_view(), name='signup'),
    path('login', views.login, name='user_login'),
    path('logout', views.logoutuser, name='logout'),    
    path('seller.register/', views.sellerregistrationform.as_view(), name='form_seller'),
    path('activate/<slug:uidb64>/<slug:token>/', views.activate, name='activate'),
]
 