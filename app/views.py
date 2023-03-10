from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
def koti(request):
    return HttpResponse('koti is Best All Rounder')
