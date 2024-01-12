from django.shortcuts import render

def index_view(request):
    return render(request,'web/index.html')

def about(request):
    return render(request,'web/about.html')


def contact(request):
    return render(request,'web/contact.html')


def elements(request):
    return render(request,'web/elements.html')

def test(request):
    return render(request,'web/test.html')