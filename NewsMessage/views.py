# -*- coding: utf-8 -*-
from NewsMessage.models import NewsMessage
from django.views.generic import ListView, DetailView

class PostsListView(ListView): # представление в виде списка
    model = NewsMessage                   # модель для представления

class PostDetailView(DetailView): # детализированное представление модели
    model = NewsMessage