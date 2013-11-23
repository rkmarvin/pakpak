from django.db import models


class Sound(models.Model):
    title = models.CharField(verbose_name=u"Название", max_length=255)
    url = models.UrlField(verbose_name=u"URl к файлу")

    class Meta:
        app_label = 'pakpak'
