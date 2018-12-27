from django.db import models

from atelieom.apps import transliterate
from django.utils import timezone
from tinymce.models import HTMLField
from photologue.models import Photo, Gallery

from django.utils.translation import gettext_lazy as _


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Caption'))
    description = HTMLField(blank=True, null=True, verbose_name=_('Description'))
    body = HTMLField(verbose_name=_('Main content'))
    slug = models.CharField(max_length=255, verbose_name=_('Slug'))
    create_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, verbose_name=_('Author'))
    external_link = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('External link'))
    photo = models.ForeignKey(Photo, on_delete=models.SET_NULL, null=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')

    # this is not needed for create link
    def save(self, *args, **kwargs):
        self.createlink()
        if not self.published_date:
            self.published_date = timezone.now()
        if not self.author:
            self.author = _('Admin of the site')
        super(Article, self).save(*args, **kwargs)

    def publish(self):
        self.published_date = timezone.now()
        if self.slug == "":
            self.slug = transliterate(self.title)
        self.save()

    def createlink(self):
        if self.slug == "":
            self.slug = transliterate(self.title)

    def __str__(self):
        return self.title
