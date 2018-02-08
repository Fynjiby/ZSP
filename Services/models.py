# -*- coding: utf-8 -*-
from django.db import models
from tinymce.models import HTMLField

class GroupServices(models.Model):
    first_name = models.CharField(max_length=100)
    text = HTMLField(blank=True)
    icone = models.FileField(upload_to = 'img/')
    
    def get_services(self):
        return Service.objects.filter(GroupServices=self)
        
    class Meta:
        verbose_name = u"Группа услуг"
        verbose_name_plural = u"Группы услуг"

    def __unicode__(self):              
        return self.first_name

class Service(models.Model):
    title = models.CharField(max_length=100)
    text = HTMLField()
    GroupServices = models.ForeignKey(GroupServices)
    
    class Meta:
        verbose_name = u"Услуга"
        verbose_name_plural = u"Услуги"

    def __unicode__(self):              
        return self.title

    