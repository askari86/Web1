from django.urls import path
from blog.views import *
app_name="blog"
urlpatterns = [
    path('',blog_home,name="blog_home"),
    path('<int:pid>',blog_single,name="single"),
    #path('post-<int:pid>',test,name='test')
]