# -*- coding:utf-8 -*-

from django.conf.urls import url

from NewsMessage.views import PostsListView, PostDetailView

from . import views

urlpatterns = [
    url(r'^$', PostsListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()),
]