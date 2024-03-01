from django.urls import path
from . import views
app_name='accounts'

urlpatterns =[
    #login
    path('login', views.login_view,name='login'),
    # logout
    path('logout', views.logout_view,name='logout'),
    # registrations
    path('singup', views.singup_view,name='singup'),
]