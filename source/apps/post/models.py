from django.db import models
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=200,
    )
    content = models.TextField(
        _('Content')
    )

    def __str__(self):
        return self.title
