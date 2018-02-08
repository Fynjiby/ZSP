# -*- coding:utf-8 -*-

from django.conf.urls import url

from license.views import PostsListView

from . import views

urlpatterns = [
    url(r'^$', PostsListView.as_view(), name='list'),
]