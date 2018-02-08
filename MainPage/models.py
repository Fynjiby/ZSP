# -*- coding: utf-8 -*-

from django.db import models
from tinymce.models import HTMLField

class MainPage(models.Model):
    title_text = models.CharField(max_length=500)
    main_text = HTMLField()
    
    class Meta:
        verbose_name = u"О компании"
        verbose_name_plural = u"О компании"

    def __unicode__(self):
        return self.title_text

    