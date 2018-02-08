# -*- coding: utf-8 -*-
from django.db import models
from tinymce.models import HTMLField

class zone(models.Model):
    title = models.CharField(max_length=100)
    html_id = models.CharField(max_length=10)
    svgpath = models.TextField()
    
    def get_projects(self):
        return project.objects.filter(zones=self)
        
    def class_zone(self):
        if project.objects.filter(zones=self).count() == 0:
            return "non-inside"
        else:
            return "inside"
    
    class Meta:
        verbose_name = u"Округ"
        verbose_name_plural = u"Округа (для интерантивной карты)"

    def __unicode__(self):              
        return self.title

class project(models.Model):
    title = models.CharField(max_length=100)
    text = HTMLField()
    zones = models.ManyToManyField(zone)

    class Meta:
        verbose_name = u"Проект"
        verbose_name_plural = u"Проекты/Объекты"

    def __unicode__(self):              
        return self.title

    