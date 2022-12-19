from django.views import View
from django.shortcuts import render

from first_dj.models import Article


class Home(View):
    @staticmethod
    def get(request):
        articles = Article.objects.all()
        return render(request, 'home.html', {"articles": articles})
