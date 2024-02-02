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
    pas=get_object_or_404(post,pk=pid,status=1)
    context={'pot':pas}
    post.counted_views+=1
    post.save()
    return render(request,'blog/blog-single.html',context,views)
    

def test(request,pid):
    pas=get_object_or_404(post,pk=pid)
    context={'pas':pas}
    return render(request,'test.html',context)
# def post_detail(request ,pid):
#     post= get_object_or_404(post , pk=pid)
#     post.increment_view_count()
#     context={'post':post}
#     return render(request,'blog/blog-home.html',context)