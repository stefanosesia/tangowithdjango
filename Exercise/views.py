from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("3ch0 says hello to the world")
