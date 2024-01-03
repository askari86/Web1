from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse('<h1>Home Page</h1>')
def about(request):
    return HttpResponse('<h2>About page</h2>')
from django.http import JsonResponse
def contact(request):
    return JsonResponse({'name':'ali'})
