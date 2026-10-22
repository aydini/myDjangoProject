
# add code for urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('aboutmyapp/', views.about, name='about'),
]