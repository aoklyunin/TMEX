from django.contrib import admin

# Register your models here.
from balance.models import Transaction


admin.site.register(Transaction)
