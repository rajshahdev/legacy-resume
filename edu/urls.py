from django.urls import  path
from .views import skill

urlpatterns = [
    path('skill/',skill, name='skill'),
]