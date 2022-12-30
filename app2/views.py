from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Aravind(request):
    return HttpResponse('This is the Aravind view of app2')
def Gouthami(request):
    return HttpResponse('<h1><marquee>This is the Gouthami view of app2</marquee></h1>')

