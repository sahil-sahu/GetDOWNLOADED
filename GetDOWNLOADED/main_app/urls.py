"""GetDOWNLOADED URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('bollywood/', views.bollywood, name='bollywood'),
    path('hollywood/', views.hollywood, name='hollywood'),
    path('pcgames/', views.pcgames, name='pcgames'),
    path('music/', views.music, name='music'),
    path('search/', views.search, name='search'),
]