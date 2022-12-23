from django.shortcuts import render
from django.views import View
from rest_framework.viewsets import ModelViewSet

from first_dj.models import Article, Category
from first_dj.serializers import CategorySerializer


class HomeView(View):
    @staticmethod
    def get(request):
        articles = Article.objects.select_related('author').prefetch_related('categories').filter(is_published=True)
        return render(request, 'home.html', {"articles": articles})


class CategoryView(ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.prefetch_related('articles').prefetch_related('articles__author').all()
