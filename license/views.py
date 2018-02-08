# -*- coding: utf-8 -*-
from license.models import license
from django.views.generic import ListView

class PostsListView(ListView): # представление в виде списка
    model = license                   # модель для представления

