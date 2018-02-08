# -*- coding:utf-8 -*-

from django import template
from Services.models import Service

register = template.Library() 
# регистрируем наш тег, который будет выводить шаблон dropdown_menu_game
@register.inclusion_tag("dropdown_menu_services.html")
def show_dropdown_menu():
    new_service = Service.objects.values('id','title').order_by("title")
    return {'new_service': new_service}

