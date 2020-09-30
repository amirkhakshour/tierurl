from django.db import models
from django.conf import settings


class ShortURL(models.Model):
    url = models.URLField(db_index=True)
    tiny_url = models.CharField(max_length=settings.SHORTENED_URL_LENGTH, unique=True)

    class Meta:
        verbose_name = 'URL Shortner'
        verbose_name_plural = 'URLs Shortner'
