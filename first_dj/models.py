from django.db import models


class Article(models.Model):
    title = models.CharField('Title', max_length=128)
    is_published = models.BooleanField('Is Published', default=True)
    content = models.TextField('Content')
