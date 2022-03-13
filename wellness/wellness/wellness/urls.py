"""wellness URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from womencare import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="home"),
    path('hairloss.html',views.hair, name="hairloss"),
    path('weight.html',views.weight, name="weight"),
    path('skin.html',views.skin, name="skin"),
    path('nutrition.html',views.nutrition, name="nutrition"),
    path('depression.html',views.depression, name="depression"),
    path('sleepdisorders.html',views.sleepdisorders, name="sleepdisorders"),
    path('weightmanagement.html',views.weightmanagement, name="weightmanagement"),
    path('workholic.html',views.workholic, name="workholic")

    
]
