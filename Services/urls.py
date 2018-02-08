# -*- coding:utf-8 -*-

from django.conf.urls import url

from Services.views import PostsListView, PostDetailView, GroupsListView, GroupDetailView

from . import views

urlpatterns = [
    url(r'^$', PostsListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()),
    url(r'^groupservices/$', GroupsListView.as_view(), name='list'),
    url(r'^groupservices/(?P<pk>\d+)/$', GroupDetailView.as_view()),
]