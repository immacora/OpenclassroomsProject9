from django.shortcuts import render
from django.http import HttpResponse


def testuser(request):
    return HttpResponse('hola')