# -*- coding:utf-8 -*-

from django import template
from projects.models import zone

register = template.Library() 
# регистрируем наш тег, который будет выводить шаблон dropdown_menu_game
@register.inclusion_tag("mini_geograthy.html")
def show_mini_geograthy():
    zone_list = zone.objects.all()
    return {'zone_list': zone_list}

