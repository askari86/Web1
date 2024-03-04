from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# app_name = 'accounts'

urlpatterns = [
    # login
    path('login/', views.login_view, name='login'),
    # logout
    path('logout/', views.logout_view, name='logout'),
    # registrations
    path('signup/', views.singup_view, name='signup'),
    # password reset
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(),name='password_change_done')
]
