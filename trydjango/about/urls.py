from django.urls import path

from . import views

# Routing in django

urlpatterns = [

    path("",views.about_view,name="about"),
    ]
