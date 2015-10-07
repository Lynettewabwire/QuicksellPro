from django.conf.urls import patterns,include, url

from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from Pro import settings
admin.autodiscover()

# urlpatterns = [
#     url(r'^$', views.index, name ='index'),
#     url(r'^register/$', views.register, name='register'),
#     url(r'^login/$', views.user_login, name='login'),
#     url(r'^index/$', views.index, name='index'),

# ]

urlpatterns = patterns('',
		url(r'^$', views.index, name ='index'),
		url(r'^login/$', views.user_login, name='login'),
 		url(r'^register/$', views.register, name='register'),
 		url(r'^account/$', views.account_details, name='account'),
 		)
		
        
# 		url(r'^finalApp/register/(?P<register_slug>[\w\-]+)/$', views.register, name ='register1'),
# 		# url(r'^finalApp/account.html/$', views.login, name='login'),
	
 		#url(r'^finalApp/add_stock.html/$', views.add_stock, name='add_stock'),
# 		url(r'^finalApp/add_stock/(?P<add_stock_slug>[\w\-]+)/$', views.add_stock, name ='add_stock'),
# 		url(r'^finalApp/cart.html/$', views.cart, name='cart'),
# 		url(r'^admin_page/$', admin, name='admin_page')
# 		)+  static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
# if settings.DEBUG:		
# 	urlpatterns += staticfiles_urlpatterns()

