from django.http import HttpResponse
from django.shortcuts import render

BASE_HTML = 'Index'


def index(request):
    return HttpResponse(BASE_HTML)


def index_plus(request, pk):
    current_html = f"{BASE_HTML + str(pk)}"
    return HttpResponse(current_html)


def index_plus_name(request, name):
    current_html = f"{BASE_HTML +' Name: '+ name}"
    return HttpResponse(current_html)
