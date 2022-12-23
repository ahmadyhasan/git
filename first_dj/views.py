from django.views import View
from django.shortcuts import render

from first_dj.models import Article


class Home(View):
    @staticmethod
    def get(request):
        articles = Article.objects.select_related('author').prefetch_related('categories').filter(is_published=True)
        return render(request, 'home.html', {"articles": articles})
