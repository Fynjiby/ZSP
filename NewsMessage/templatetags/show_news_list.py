# -*- coding:utf-8 -*-

from django import template
from NewsMessage.models import NewsMessage

register = template.Library() 
# регистрируем наш тег, который будет выводить шаблон dropdown_menu_game
@register.inclusion_tag("news_list.html")
def show_news_list():
    news_list = NewsMessage.objects.values('id','title','published_date').order_by("-published_date")[:3]
    return {'news_list': news_list}

