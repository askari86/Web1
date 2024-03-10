from django.shortcuts import render,get_object_or_404,redirect
from blog.models import post,comment
from django.utils import timezone
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from blog.forms import CommentForm
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def blog_home(request,**kwargs):
    currnt_time=timezone.now()
    posts=post.objects.filter(status=1,publish_date__lte=currnt_time)
    if kwargs.get('cat_name') != None:
        posts=posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('tag_name') != None:
        posts=posts.filter(tags__name__in=[kwargs['tag_name']])
    if kwargs.get('author_username') != None:
        posts=posts.filter(author__username =kwargs['author_username'])
    posts=Paginator(posts,3)
    try:
        page_number=request.GET.get('page')
        posts=posts.get_page(page_number)
    except PageNotAnInteger:
        posts=posts.get_page(1)
    except EmptyPage:
        posts=posts.get_page(1)
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Your comment has been registered. Then the review will be displayed')
        else:
            messages.add_message(request,messages.ERROR,'your tikct didnt submited')
    currnt_time=timezone.now()
    pas=get_object_or_404(post,pk=pid,status=1,publish_date__lte=currnt_time)
    next_post = post.objects.filter(id__gt=pid, status=1, publish_date__lte=currnt_time).order_by('id').first()
    prev_post = post.objects.filter(id__lt=pid, status=1, publish_date__lte=currnt_time).order_by('-id').first()
    pas.counted_views+=1
    pas.save()
    if pas.login_require==False:
        comments=comment.objects.filter(post=pas.id,approwed=True)
        form=CommentForm()
        context={'pot':pas,'comments':comments,'next_post':next_post,'prev_post':prev_post,'form':form}
        return render(request,'blog/blog-single.html',context)  
    elif pas.login_require==True and request.user.is_authenticated:
        pas.login_require=False
        comments=comment.objects.filter(post=pas.id,approwed=True)
        form=CommentForm()
        context={'pot':pas,'comments':comments,'next_post':next_post,'prev_post':prev_post,'form':form}
        return render(request,'blog/blog-single.html',context)
    return HttpResponseRedirect(reverse('accounts:login'))


# def test(request,pid):
#     pas=get_object_or_404(post,pk=pid)
#     context={'pas':pas}
#     return render(request,'train-if.html',context)

def blog_category(request,cat_name):
    currnt_time=timezone.now()
    posts=post.objects.filter(status=1,publish_date__lte=currnt_time)
    posts=posts.filter(category__name=cat_name)
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_search(request):
    currnt_time=timezone.now()
    posts=post.objects.filter(status=1,publish_date__lte=currnt_time)
    if request.method == 'GET':
        if  s:= request.GET.get('s'):
            posts=posts.filter(content__contains= s) 
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)
