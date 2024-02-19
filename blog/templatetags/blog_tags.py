from django import template
from blog.models import post
from blog.models import Category
from django.utils import timezone
register=template.Library()

@register.simple_tag(name='plus')
def function(a=5):
    return a+2

@register.simple_tag(name='totalpost')
def total():
    posts=post.objects.filter(status=1).count()
    return posts

@register.simple_tag(name='posts')
def total():
    posts=post.objects.filter(status=1)
    return posts

@register.filter
def snippet(value,arg=70):
    return  value[:arg]+"..."

@register.inclusion_tag('blog/blog-papular-post.html')
def lastposts(arg=3):
    posts=post.objects.filter(status=1).order_by('publish_date')
    return {'posts':posts}

@register.inclusion_tag('blog/blog-categorys-post.html')
def postcategotys():
    posts=post.objects.filter(status=1)
    category=Category.objects.all()
    cat_dict ={}
    for name in category:
       cat_dict[name]=posts.filter(category=name).count()
    return {'categ':cat_dict}

@register.inclusion_tag('web/index-Latestfrom.html')
def recent():
    currnt_time=timezone.now()
    posts=post.objects.filter(status=1,publish_date__lte=currnt_time).order_by('publish_date')[:4]
    context={'posts': posts}
    return context

