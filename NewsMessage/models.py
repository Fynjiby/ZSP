# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField


class NewsMessage(models.Model):
    title = models.CharField(max_length=500)
    text = HTMLField()
    published_date = models.DateTimeField(
            blank=True, null=True)

    class Meta:
        verbose_name = u"Новость"
        verbose_name_plural = u"Новости"
        

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title