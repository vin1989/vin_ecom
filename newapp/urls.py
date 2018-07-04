
from django.conf.urls import url

from .views import *

urlpatterns = [
    
    url(r'^$',home,name='home'),
    url(r'^auth-check/$',auth_view,name='check'),
    url(r'^invalid/$',invalid_login),
    url(r'^logout/$',logout,name='logout'),
    url(r'^signup/$', signup, name='signup'),
]
