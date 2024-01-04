
from django.contrib import admin
from django.urls import path, include
from core import docs 

urlpatterns = [
    path('', include('core.docs')), 
]
