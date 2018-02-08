# -*- coding:utf-8 -*-

from django import template
from Services.models import GroupServices

register = template.Library() 
@register.inclusion_tag("group_services.html")
def show_group_services():
    groups = GroupServices.objects.values('id','first_name','icone').order_by("id")
    return {'groups': groups}
