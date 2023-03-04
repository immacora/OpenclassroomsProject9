from django.shortcuts import render
from django.http import HttpResponse


def feeds(request):
    return HttpResponse('hello')