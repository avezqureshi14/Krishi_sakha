from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('input/', views.input, name='input'),
    path('RESULT/', views.RESULTS, name='result'),


    
]


