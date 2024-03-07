from django.urls import path 
from . import views


urlpatterns = [ 
    path("", views.homepage, name="homepage"),
    path("/membership", views.memberpage, name="membership"),
    ]