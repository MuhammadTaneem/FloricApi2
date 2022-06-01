from django.urls import include, path
from rest_framework import routers
from .views import ProductViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register('list', ProductViewSet)
router.register('category', CategoryViewSet)


urlpatterns = [
    path('', include(router.urls)),
]