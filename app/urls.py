from django.urls import path 
from django.contrib import admin
from . import views


urlpatterns = [ 
    path("", views.coverpage, name="coverpage"),            
    path("home", views.homepage, name="homepage"),
    path("membership", views.memberpage, name="membership"),
    path("officerslogin", views.officerslogin, name="officerslogin"),
    
    ]