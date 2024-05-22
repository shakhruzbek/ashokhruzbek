from django.contrib import admin

from .models import Company, Service, Staff

# Register your models here.
admin.site.register([Company, Staff, Service])