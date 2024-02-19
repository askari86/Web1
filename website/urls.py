from django.urls import path
from website.views import *
app_name="website"
urlpatterns = [
    path('',index_view,name="index"),
    path('about',about,name="about"),
    path('contact',contact,name="contact"),
    path('test',test,name="test"),
    path('newsletter',newsletter,name="newsletter")
]