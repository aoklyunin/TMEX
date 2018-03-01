from __future__ import unicode_literals

from django.db import models

# Create your models here.

# класс транзакции
from django.utils import timezone

from personal.models import Consumer


class Transaction(models.Model):
    value = models.IntegerField(default=0)
    consumer = models.ForeignKey(Consumer)
    dt = models.DateTimeField(default=timezone.now())
    comment = models.CharField(max_length=1000, default="")

    def __unicode__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)

