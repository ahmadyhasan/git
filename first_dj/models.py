from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    title = models.CharField('Title', max_length=64)


class Article(models.Model):
    title = models.CharField('Title', max_length=128)
    is_published = models.BooleanField('Is Published', default=True)
    content = models.TextField('Content')
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    categories = models.ManyToManyField(Category)
