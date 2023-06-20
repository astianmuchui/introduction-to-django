from django.shortcuts import render
from .models import Question, Choice

# Create your views here.


# Get questions

def index(request):

    return(render(request, 'polls/index.html'))