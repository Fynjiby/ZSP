# -*- coding: utf-8 -*-
from Services.models import Service, GroupServices
from django.views.generic import ListView, DetailView

class PostsListView(ListView): # представление в виде списка
    model = Service                   # модель для представления

class PostDetailView(DetailView): # детализированное представление модели
    model = Service
    
class GroupsListView(ListView): # представление в виде списка
    model = GroupServices                   # модель для представления

class GroupDetailView(DetailView): # детализированное представление модели
    model = GroupServices