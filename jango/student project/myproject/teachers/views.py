from django.shortcuts import render
from django.http import HttpResponse
from .models import teacher
# Create your views here.
def home(request):
    return HttpResponse("welcome to teacher page")
def details(request):
    t = teacher.objects.all()
    return HttpResponse(t)