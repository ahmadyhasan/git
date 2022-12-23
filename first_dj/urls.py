from django.contrib import admin
from django.urls import path, include

from first_dj.views import HomeView, CategoryView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'categories', CategoryView, basename='category')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('', HomeView.as_view()),
    path('admin/', admin.site.urls),
]
