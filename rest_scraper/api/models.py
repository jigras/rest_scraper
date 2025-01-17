from django.db import models
from django.utils.timezone import now

class Page(models.Model):
    """
    Page scraping model
    """
    url = models.CharField(verbose_name='Url strony', max_length=2048,
                           help_text='Adres url strony z protokołem http/https')
    text = models.TextField(verbose_name='Tekst ze strony', null=True, blank=True)
    scraped_at = models.DateTimeField(null=True, blank=True,verbose_name='Scrawlowany o')
    scraped = models.BooleanField(default= False, verbose_name='Gotowy-scrawlowany')
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.url

    class Meta:
        ordering = ['id']
        verbose_name = "Strona"
        verbose_name_plural = "Strony"


class Picture(models.Model):
    """
    Scraped picture model
    """
    page = models.ForeignKey(Page, on_delete=models.CASCADE, verbose_name='Strona')
    picture = models.ImageField(upload_to='media', verbose_name='Obraz')
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.picture.name

    class Meta:
        ordering = ['id']
        verbose_name = "Obraz"
        verbose_name_plural = "Obrazy"
