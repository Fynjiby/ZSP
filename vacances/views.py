# -*- coding: utf-8 -*-
from vacances.models import vacance
from django.views.generic import ListView, DetailView

class PostsListView(ListView): # представление в виде списка
    model = vacance                   # модель для представления

class PostDetailView(DetailView): # детализированное представление модели
    model = vacance