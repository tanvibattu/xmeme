from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from rest_framework import routers
from meme import views                           

urlpatterns = [
    path('admin/', admin.site.urls),  
    #   go to meme_list view when url is with /memes or /memes/
    url(r'^memes$', views.meme_list),
    url(r'^memes/$', views.meme_list),
    #   go to meme_detail to show meme with particular id
    url(r'^memes/(?P<id>[0-9]+)$', views.meme_detail),    
    
]