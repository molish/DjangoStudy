from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (self):
    return HttpResponse("<h3>Hello world!</h3>")
