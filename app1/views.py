from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request, 'a.html', {'link': 'http://127.0.0.1:8000/'})


def calloption(request):
    return render(request, 'call_index.html')


def putoption(request):
    return render(request, 'put_index.html')
