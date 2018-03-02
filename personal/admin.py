from django.contrib import admin

# Register your models here.
from personal.models import Consumer, Company

admin.site.register(Company)
admin.site.register(Consumer)
