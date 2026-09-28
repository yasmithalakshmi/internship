from django.shortcuts import render
from django.http import HttpResponse
from .models import attend
# Create your views here.
def home(request):
    return HttpResponse("welcome to attendance page")
def details(request):
    a = attend.objects.all()
    return HttpResponse(a)