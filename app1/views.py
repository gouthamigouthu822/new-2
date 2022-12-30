from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('This is the first view of app1')
def second(request):
    return HttpResponse('This is the second view of app1')
