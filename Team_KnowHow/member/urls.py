from django.conf.urls import url, include
from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('member_register', views.member_register, name="member_register"),
]