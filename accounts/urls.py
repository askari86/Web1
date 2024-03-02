from django.urls import path
from . import views
from django.contrib.auth import views as Views
app_name='accounts'

urlpatterns =[
    #login
    path('login', views.login_view,name='login'),
    # logout
    path('logout', views.logout_view,name='logout'),
    # registrations
    path('singup', views.singup_view,name='singup'),
    #password
    path('password_reset/', Views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', Views.PasswordResetDoneView.as_view(template_name='registration:password_reset_done'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', Views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', Views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
]