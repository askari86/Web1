from django.shortcuts import render
from blog.models import post
from django.utils import timezone
from website.models import Contact


def index_view(request):
    currnt_time=timezone.now()
    posts=post.objects.filter(status=1,publish_date__lte=currnt_time)
    context={'posts':posts}
    return render(request,'web/index.html',context)

def about(request):
    return render(request,'web/about.html')


def contact(request):
    return render(request,'web/contact.html')

def test(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        c = Contact()
        c.name = name
        c.email = email
        c.subject = subject
        c.message = message
        c.save()

    return render(request,'test.html',{})