from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def app1view(request):
    return HttpResponse('<h1>hello world app1</h>')