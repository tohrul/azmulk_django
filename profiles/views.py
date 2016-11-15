from django.shortcuts import render
from django.http imoprt HttpResponse

def index(request):
    return HttpResponse("You are at profilse index.")

