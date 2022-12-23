from django.contrib.auth import get_user_model
from rest_framework import serializers

from first_dj.models import Category, Article

User = get_user_model()


class UserMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class ArticleMinimalSerializer(serializers.ModelSerializer):
    author = UserMinimalSerializer()

    class Meta:
        model = Article
        fields = ('id', 'title', 'author')


class CategorySerializer(serializers.ModelSerializer):
    articles = ArticleMinimalSerializer(many=True)

    class Meta:
        model = Category
        fields = ('id', 'title', 'articles')
