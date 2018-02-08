# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import license, groupLicenseImg, licenseImg

admin.site.register(license)
admin.site.register(groupLicenseImg)
admin.site.register(licenseImg)