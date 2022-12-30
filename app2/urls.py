from django.urls import path
from app2.views import *
app_name='Something 2'
urlpatterns=[
    path('Aravind/',Aravind,name='Aravind'),
    path('Gouthami/',Gouthami,name='Gouthami'),
]