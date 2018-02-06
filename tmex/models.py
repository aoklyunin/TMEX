# -*- coding: utf-8 -*-


import mistune
import re
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone
from gunicorn.config import User
from mptt.models import MPTTModel, TreeForeignKey
from tmex_main.utils.model_utils import ContentTypeAware, MttpContentTypeAware


class Company(models.Model):
    # название компании
    name = models.CharField(max_length=100,default="",blank=True,none=True)
    # инн
    inn = models.CharField(max_length=10,default="",blank=True,none=True)
    # КПП
    kpp = models.CharField(max_length=10,default="",blank=True,none=True)
    # ОГРН
    ogrn = models.CharField(max_length=9,default="",blank=True,none=True)
    # юридический адрес
    jurAddress = models.CharField(max_length=400,default="",blank=True,none=True)
    # физический адрес
    fisicAddress   = models.CharField(max_length=400,default="",blank=True,none=True)
    # Р/С
    rs = models.CharField(max_length=9, default="", blank=True, none=True)


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
    companies = models.ManyToManyField(Company,blank=True,none=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
