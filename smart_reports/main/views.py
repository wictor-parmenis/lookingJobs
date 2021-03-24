from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(response):
    return HttpResponse('<h1>Report Job</h1>')


def newsletter(response):
    return HttpResponse('<h1>Newsletter here</h1>')