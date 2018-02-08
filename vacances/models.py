# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField


class vacance(models.Model):
    title = models.CharField(max_length=200)
    text = HTMLField()
    
    class Meta:
        verbose_name = u"Вакансия"
        verbose_name_plural = u"Вакансии"
        

    def __unicode__(self):
        return self.title