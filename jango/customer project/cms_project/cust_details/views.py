from django.shortcuts import render
from django.http import HttpResponse
from .models import cust_detail
# Create your views here.
def home(request):
    c = cust_detail.objects.all()
    return HttpResponse("welcome to home page")
    return HttpResponse(c)
