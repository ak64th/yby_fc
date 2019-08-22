from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Post(models.Model):
    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True)
    updated = models.DateTimeField(_('updated'), default=timezone.now)
    published = models.BooleanField(_('published'), default=False)

    class Meta:
        verbose_name = _("post")
