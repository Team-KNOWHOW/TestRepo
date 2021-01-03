from django.conf.urls import url, include
from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name="home"),

    path('cb_code', views.cb_code, name="cb_code"),
    path('codetype_insert', views.codetype_insert, name="codetype_insert"),
    path('codetype_update', views.codetype_update, name="codetype_update"),
    path('codetype_delete', views.codetype_delete, name="codetype_delete"),
    ]