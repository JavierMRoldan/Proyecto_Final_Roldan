from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
# Create your views here.


def home(request):

    return render(request, "home.html")

def principal(request):

    return render(request, "padre.html")

def about(request):

    return render(request, "about.html")