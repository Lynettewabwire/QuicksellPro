"""Pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from finalApp import urls as finalApp_urls
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from finalApp import views
if settings.DEBUG:
	admin.autodiscover()

# urlpatterns = [
#     url(r'^register/$', views.register, name='register'),
#     url(r'^login/$', views.user_login, name='login'),
#     url(r'^index/$', views.index, name='index'),
#     url(r'^admin/', include(admin.site.urls)),
# ]

urlpatterns = [
    url (r'^finalApp/', include(finalApp_urls, namespace='finalApp')),
 	url(r'^admin/', include(admin.site.urls)),
	   
 ] + static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)

