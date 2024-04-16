from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.db.models import Avg, Count
from django.core.validators import MaxValueValidator, MinValueValidator

User = get_user_model()


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

    @property
    def get_avg_score(self):
        return self.post.aggregate(Avg('score'))

    @property
    def get_number_user_score(self):
        return self.post.aggregate(Count('user'))


class PostScore(models.Model):
    user = models.ForeignKey(
        to=User,
        verbose_name=_('User'),
        on_delete=models.CASCADE,
        related_name='user'
    )
    post = models.ForeignKey(
        to=Post,
        verbose_name=_('Post'),
        on_delete=models.CASCADE,
        related_name='post'
    )
    score = models.SmallIntegerField(
        _('Score'),
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    created_on = models.DateTimeField(
        _('created on'),
        auto_now_add=True
    )

    class Meta:
        ordering = ['-created_on']
        verbose_name = _('post_score')
        verbose_name_plural = _('post_scores')

    def __str__(self):
        return str(self.score)
