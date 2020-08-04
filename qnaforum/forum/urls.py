from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('result', views.result, name = 'result'),
    path('fetch', views.fetch, name = 'fetch')
]
