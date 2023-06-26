from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def main(request):
    template = loader.get_template('index.html')
    context = {}
    
    return HttpResponse(template.render(context, request))

def members(request):
    template = loader.get_template('members.html')
    context = {}
    return HttpResponse(template.render(context, request))