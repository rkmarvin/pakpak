# coding: utf-8
from django.db import models


class Sound(models.Model):
    title = models.CharField(verbose_name=u"Название", max_length=255)
    url = models.URLField(verbose_name=u"URl к файлу")
