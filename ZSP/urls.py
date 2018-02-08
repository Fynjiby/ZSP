"""ZSP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import *
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^$',TemplateView.as_view(template_name='start.html')),
    url(r'^services/', include('Services.urls', namespace="Services")),
    url(r'^news/', include('NewsMessage.urls', namespace="NewsMessage")),
    url(r'^licenses/', include('license.urls', namespace="license")),
    url(r'^vacances/', include('vacances.urls', namespace="vacances")),
    url(r'^contacts/', include('contacts.urls', namespace="contacts")),
    url(r'^projects/', include('projects.urls', namespace="projects")),
    url(r'^geograthy/', include('projects.urls', namespace="geograthy")),
]

