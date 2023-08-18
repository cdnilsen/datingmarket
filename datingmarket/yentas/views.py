from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import EndUser


def index(request):
    return HttpResponse("Hello, world. You're at the yentas index.")
# Create your views here.
class User():
    se