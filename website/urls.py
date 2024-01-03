from django.urls import path
from website.views import index,about,contact
urlpatterns = [
    path('home' , index),
    path('about' , about),
    path('contact',contact)
]