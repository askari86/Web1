from django.shortcuts import render,get_object_or_404
from blog.models import post
from django.utils import timezone
# Create your views here.
def blog_home(request):
    currnt_time=timezone.now()
    filter_post=post.objects.filter(status=1,publish_date__lte=currnt_time)
    context={'posts':filter_post}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    currnt_time=timezone.now()
    pas=get_object_or_404(post,pk=pid,status=1,publish_date__lte=currnt_time)
    next_post = post.objects.filter(id__gt=pid, status=1, publish_date__lte=currnt_time).order_by('id').first()
    prev_post = post.objects.filter(id__lt=pid, status=1, publish_date__lte=currnt_time).order_by('-id').first()
    pas.counted_views+=1
    pas.save()
    context={'pot':pas,'next_post':next_post,'prev_post':prev_post}
    return render(request,'blog/blog-single.html',context)
    

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
