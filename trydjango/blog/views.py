from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def blog_view(request):
    template = loader.get_template('blog.html')
    return HttpResponse(template.render())

def blog_home_view(request):
    return HttpResponse("Blog Home View")

def blog_single_view(request, id):
    return HttpResponse("Blog Single View "+str(id))