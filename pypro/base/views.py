from django.http import HttpResponse  # uso implícito
from django.shortcuts import render


def home(request):
    return render(request, 'base/home.html')
