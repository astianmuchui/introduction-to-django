from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def members(request):
    temp = loader.get_template('myfirst.html')
    return HttpResponse(temp.render())

def home(request):
    temp = loader.get_template('home.html')
    return HttpResponse(temp.render())