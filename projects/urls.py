# -*- coding:utf-8 -*-

from django.conf.urls import url

from projects.views import PostsListView, PostDetailView, GeogView

from . import views

urlpatterns = [
    url(r'^$', PostsListView.as_view(), name='list'),
    #url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()),
    url(r'^geograthy/$', GeogView.as_view(), name='geograthy'),
]