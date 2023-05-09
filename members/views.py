from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from members.models import Member
# Create your views here.

def members(request):
    members = Member.objects.all().values()
    temp = loader.get_template('all_members.html')
    context = {
        "members": members
    }
    return HttpResponse(temp.render(context, request))

def home(request):
    temp = loader.get_template('home.html')
    return HttpResponse(temp.render())

def details(request, id):
    temp = loader.get_template('details.html')
    member = Member.objects.get(id=id)
    context = {
        "member": member
    }
    return HttpResponse(temp.render(context, request))

