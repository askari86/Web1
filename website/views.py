from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'web/index.html')

def about(request):
    return render(request,'web/about.html')


def contact(request):
    return render(request,'web/contact.html')
