from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import CategoryViewSet, BrandViewSet, ProductViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register('category', CategoryViewSet)
router.register('brand', BrandViewSet)
router.register('product', ProductViewSet)
router.register('order', OrderViewSet)

urlpatterns = [
    path('', include(router.urls))
]