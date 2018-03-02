from django.contrib import admin

# Register your models here.
from support.models import Message, SupportTread

admin.site.register(Message)
admin.site.register(SupportTread)
