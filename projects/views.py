# -*- coding: utf-8 -*-
from projects.models import project,zone
from django.views.generic import ListView, DetailView

class PostsListView(ListView): # представление в виде списка
    model = project                   # модель для представления

class PostDetailView(DetailView): # детализированное представление модели
    model = project
    
class GeogView(ListView): # представление в виде списка
    model = zone                   # модель для представления