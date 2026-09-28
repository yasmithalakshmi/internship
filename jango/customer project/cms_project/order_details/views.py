from django.shortcuts import render
from django.http import HttpResponse
from .modeks import order
# Create your views here.
def home(request):
    o = order.objects.all()
    return HttpResponse(o)