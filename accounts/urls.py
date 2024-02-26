from django.urls import path
from . import views
app_name='accounts'

urlpatterns =[
    #login
    path('login', views.login,name='login'),
    # logout
    # path('logout', views.logout,name='logout'),
    # registrations
    path('singup', views.singup,name='singup'),
]