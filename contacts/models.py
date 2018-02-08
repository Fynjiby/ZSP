# -*- coding: utf-8 -*-
from django.db import models
from tinymce.models import HTMLField
from django import forms

class contact(models.Model):
    title = models.CharField(max_length=50)
    text = HTMLField()
    yaMaps = HTMLField()
    
    class Meta:
        verbose_name = u"Контант"
        verbose_name_plural = u"Контанты"
    
    def __unicode__(self):              
        return self.title

