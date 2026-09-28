from django.shortcuts import render
from django.http import HttpResponse
from .models import student
# Create your views here.
def home(request):
    return HttpResponse("welcome to student page")
def details(request):
    s_list = student.objects.all()
    return HttpResponse(s_list)
    