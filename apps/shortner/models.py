from django.db import models
from django.conf import settings
from .services import gen_random_alphanum_string


class ShortURL(models.Model):
    url = models.URLField(db_index=True)
    tiny_url = models.CharField(max_length=settings.SHORTENED_URL_LENGTH, unique=True)

    class Meta:
        verbose_name = 'URL Shortner'
        verbose_name_plural = 'URLs Shortner'

    def save(self, *args, **kwargs):
        if not self.tiny_url:
            self.tiny_url = gen_random_alphanum_string()
            while self.__class__.objects.filter(tiny_url=self.tiny_url).exists():
                self.tiny_url = gen_random_alphanum_string()
        super(ShortURL, self).save(*args, **kwargs)
