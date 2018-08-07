from django.contrib import admin
from django.conf.urls import url,include
from loginapp.views import thanks
from loginapp.views import index
from loginapp.views import addemail

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^thanks/',thanks),
    url(r'^$',index),
    url(r'^addemail/',addemail),
]
