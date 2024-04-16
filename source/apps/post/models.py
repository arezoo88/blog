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
    created_on = models.DateTimeField(
        _('created on'),
        auto_now_add=True
    )

    class Meta:
        ordering = ['-created_on']
        verbose_name = _('post')
        verbose_name_plural = _('posts')

    def __str__(self):
        return self.title
