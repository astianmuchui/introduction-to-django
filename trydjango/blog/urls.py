from django.urls import path
from . import views
urlpatterns = [
    path("",views.blog_view,name="blog"),
    path("home/",views.blog_home_view,name="blog-home"),
    path("single/<int:id>/",views.blog_single_view,name="blog-single"),
]