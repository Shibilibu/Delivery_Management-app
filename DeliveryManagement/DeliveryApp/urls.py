"""DeliveryManagement URL Configuration

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

from DeliveryApp import views

urlpatterns = [
    path('',views.login_page),
    path('login_to_app',views.login_to_app),
########################################Admin##########################################################
    path('admin_page',views.admin_page),
    path('details_view',views.details_view),
#######################################Delivery_Person##################################################
    path('delivery_per',views.delivery_per),
    path('signup_form',views.signup_form),
    path('capture_page',views.capture_page),
    path('store_captured',views.store_captured),
    path('password_change_page',views.password_change_page),
    path('forget_pswd',views.forget_pswd),
    path('capture',views.capture),




]
