from django.contrib.auth.models import User
from django.db import models

# Create your models here.



# обращение в техподдержку
from django.utils import timezone


class SupportTread(models.Model):
    handle = models.CharField(max_length=100)
    author = models.ForeignKey(User)


# сообщение
class Message(models.Model):
    dt = models.DateTimeField(default=timezone.now())
    author = models.ForeignKey(User, related_name='author')
    target = models.ForeignKey(User, related_name='target')
    supportTread = models.ForeignKey(SupportTread)
