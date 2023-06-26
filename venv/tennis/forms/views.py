from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.

def index(request):
    template = loader.get_template('forms.html')
    context = {}

    if isinstance(request.POST, dict): # if request.POST is a dictionary
        context['name'] = request.POST.get('name')

    return HttpResponse(template.render(context,request))