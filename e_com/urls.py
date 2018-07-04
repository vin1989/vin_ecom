
from django.conf.urls import url,include
from django.contrib import admin
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^e_comm_login/',include('newapp.urls',namespace='login_app')),
    url(r'^$',index),
    url(r'^search/$',search),
    url(r'^checkout/$',check_out,name='checkout'),
    url(r'^shop/$',shop),
    url(r'^delete/(\d+)/$',delete_item,name='delete'),
    url(r'^cart_detail/$',cart_detail,name='cart_detail'),
    
    url(r'^product_detail/(\d+)/$',product_detail,name='detail'),

    #http://127.0.0.1:8000/shop/tables/
    url(r'^shop/(\w+)/$',Single_category,name='category')
] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)
