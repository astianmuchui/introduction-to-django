from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def blog_view(request):
    return HttpResponse("Blog View")

def blog_home_view(request):
    return HttpResponse("Blog Home View")

def blog_single_view(request, id):
    return HttpResponse("Blog Single View "+str(id))