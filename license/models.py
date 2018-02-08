# -*- coding: utf-8 -*-
from django.db import models
from tinymce.models import HTMLField

class license(models.Model):
    title = models.CharField(max_length=150)
    text = HTMLField()
    
    def get_group_img(self):
        return groupLicenseImg.objects.filter(license=self)
        
    class Meta:
        verbose_name = u"Лицензия"
        verbose_name_plural = u"Лицензии"
    
    def __unicode__(self):              
        return self.title

        
class groupLicenseImg(models.Model):
    title = models.CharField(max_length=150)
    license = models.ForeignKey(license)
    
    def get_img(self):
        return licenseImg.objects.filter(group=self)
    
    class Meta:
        verbose_name = u"Группа картинок лицензии"
        verbose_name_plural = u"Группы картинок лицензий"
    
    def __unicode__(self):              
        return self.title

        
class licenseImg(models.Model):
    title = models.CharField(max_length=150)
    img = models.ImageField(upload_to = 'img/')
    group = models.ForeignKey(groupLicenseImg)
    
    class Meta:
        verbose_name = u"Картинка лицензии"
        verbose_name_plural = u"Картинки лицензий"
    
    def __unicode__(self):              
        return self.title