from django.shortcuts import render
from django.http import HttpResponse

# Create your views here for url patterns
def index(request):
    #add code to show Hello World on the index page
    # edit line below to display Hello World on django server without index.html page
    return HttpResponse('<h1>Hello World</h1>')

def about(request):
    #add code to show about page
    return HttpResponse('<h2>This is the about page of my Django application.</h2>')