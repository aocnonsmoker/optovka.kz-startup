from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import UserViewSet

router = routers.DefaultRouter()
router.register('profile', UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]