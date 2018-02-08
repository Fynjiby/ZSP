# -*- coding:utf-8 -*-

import random
from django import template
from MainPage.models import MainPage

register = template.Library() 
@register.inclusion_tag("About_Company.html")
def show_about_company():
    AboutCompanys = MainPage.objects.values('id','title_text','main_text').order_by("id")[:1]
    return {'AboutCompanys': AboutCompanys}

