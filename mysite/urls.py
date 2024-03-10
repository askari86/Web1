"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include ,re_path
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import StaticViewSitemap
from blog.sitemaps import BlogSitemap
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar
from django.views.generic import TemplateView

sitemaps = {
    'static': StaticViewSitemap,
    'blog': BlogSitemap
}

urlpatterns = [
    re_path(r'^', TemplateView.as_view(template_name='home.html')),
    path('admin/', admin.site.urls),
    #account
    path('accounts/',include('accounts.urls')),
    #index
    path('',include('website.urls')),
    #blog
    path('blog/',include('blog.urls')),
    #sitemap
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    #summernote
    path('summernote/', include('django_summernote.urls')),
    #robots
    path('robots.txt', include('robots.urls')),
    #captcha
    path('captcha/', include('captcha.urls')),
    #debug
    path("__debug__/", include("debug_toolbar.urls")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
