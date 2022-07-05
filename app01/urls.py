from django.contrib import admin
from django.urls import path,include
from app01 import views

urlpatterns = [
    path('send/sms/',views.send_sms ),
    path('send/register/',views.register ),

]
