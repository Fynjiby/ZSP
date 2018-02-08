# -*- coding:utf-8 -*-

from django.conf.urls import url

#from contacts.views import PostsListView

from . import views

urlpatterns = [
    #url(r'^$', PostsListView.as_view(), name='list'),
    url(r'^$', views.contactView),
]