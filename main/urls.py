from django.contrib import admin
from django.urls import path, include
from .views import Home

appname = "main"
urlpatterns = [
    path('', Home.as_view(), name='home'),
]
