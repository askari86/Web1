from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from blog.models import post
from django.utils import timezone
from website.models import Contact
from website.forms import Nameform,ContactForm,newslettr
from django.contrib import messages

def index_view(request):
    currnt_time=timezone.now()
    posts=post.objects.filter(status=1,publish_date__lte=currnt_time)
    context={'posts':posts}
    return render(request,'web/index.html',context)

def about(request):
    return render(request,'web/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.name = "ananymous"
            contact.save()
            messages.add_message(request,messages.SUCCESS,'your tikct submited successfuly')
        else:
            messages.add_message(request,messages.ERROR,'your tikct didnt submited')
    else:
        form = ContactForm()
    return render(request, 'web/contact.html', {'form': form})


def newsletter(request):
    if request.method == 'POST':
        form=newslettr(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your tikct submited successfuly')
            return HttpResponseRedirect('blog/')
    else:
        messages.add_message(request,messages.ERROR,'your tikct didnt submited')
        return HttpResponseRedirect('blog/')

        


def test(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done')
            
        else:
            return HttpResponse('not valid')
    form = ContactForm()
    return render(request,'test.html',{'form':form})