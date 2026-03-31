from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from subscriptions.views import SubscriptionViewSet

# Создаём роутер
router = DefaultRouter()
router.register(r'subscriptions', SubscriptionViewSet, basename='subscription')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # API эндпоинты
]