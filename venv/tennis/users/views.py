from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.template import loader
# Create your views here.

def index(request):
    # Check for submit
    if request.POST:
        save = models.User(uname=request.POST.get('name'), email=request.POST.get('email'))
        save.save()

    return HttpResponse(render(request, 'users.html',{}))

def users(request):

    # FETCH all users order by ido
    usrs = models.User.objects.all().order_by('-id')

    template = loader.get_template('view.html')
    context = {
        'users': usrs,
    }

    return HttpResponse(template.render(context, request))