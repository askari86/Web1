from django.shortcuts import render

# Create your views here.
def blog_home(request):
    return render(request,'blog/blog-home.html')

def blog_single(request):
    context={'title':'bitcoin crash again!','content':'bro bitcoin bekhaaaaaaaaar gron mishe','authot':'Iliya Askari'}
    return render(request,'blog/blog-single.html',context)