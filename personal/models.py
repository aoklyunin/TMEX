from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# класс компании
class Company(models.Model):
    # название компании
    name = models.CharField(max_length=100, default="", blank=True)
    # инн
    inn = models.CharField(max_length=10, default="", blank=True)
    # КПП
    kpp = models.CharField(max_length=10, default="", blank=True)
    # ОГРН
    ogrn = models.CharField(max_length=9, default="", blank=True)
    # юридический адрес
    jurAddress = models.CharField(max_length=400, default="", blank=True)
    # физический адрес
    fisicAddress = models.CharField(max_length=400, default="", blank=True)
    # Р/С
    rs = models.CharField(max_length=9, default="", blank=True)
    # БИК
    bik = models.CharField(max_length=9, default="", blank=True)
    # банк
    b = models.CharField(max_length=100, default="", blank=True)
    # к/с
    ks = models.CharField(max_length=30, default="", blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


# класс заказчика
class Consumer(models.Model):
    # предприятие
    TP_COMPANY = 0
    # патентный поверенный
    TP_WORKER = 1

    # русский язык
    LANGUAGE_RUSSIAN = 0
    # английский язык
    LANGUAGE_ENGLISH = 1

    # ФИО
    name = models.CharField(max_length=400, default="")
    # пользователь
    user = models.OneToOneField(User)
    # тип пользователя
    tp = models.IntegerField(default=0)
    # язык
    language = models.IntegerField(default=0)
    # телефон
    tel = models.CharField(max_length=20, default="")

    # название для отчётов
    reportName = models.CharField(max_length=300, default="")
    # адрес офиса
    reportAddress = models.CharField(max_length=300, default="")
    # телефон для обратной связи
    reportTel = models.CharField(max_length=20, default="")
    # почта для обратной связи
    reportMail = models.EmailField(default="")
    # логотип
    logo = models.ImageField(upload_to='avatars/', null=True)
    # баланс
    balance = models.IntegerField(default=0)
    # компании
    companies = models.ManyToManyField(Company, blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

