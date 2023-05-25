from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    base_html = '<h1>Index!</h1>'
    return HttpResponse(base_html)
