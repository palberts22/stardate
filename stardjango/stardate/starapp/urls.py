from django.urls import path, include
import starapp
from starapp.views import AspectsView
from starapp.views import AdminLogin
from django.contrib import admin
from starapp.views import register


app_name = 'starapp'
urlpatterns = [
    path('', starapp.views.index, name='index'),
    path('login/', AdminLogin.as_view(), name='login'),
    path('aspects/', AspectsView.as_view(), name="aspects"), 
    path('register/', register, name="register"),
]