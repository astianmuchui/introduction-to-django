from django.urls import path

from . import views

# to handle urls for polls/*

urlpatterns = [
    path('', views.index, name='index'),
]
