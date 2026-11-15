from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    return render(request, 'home/home.html')


def health_check(request):
    return HttpResponse("OK")