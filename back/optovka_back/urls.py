from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token
from user.views import CustomObtainAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('market/', include('market.urls')),
    path('user/', include('user.urls')),
    path('auth/', CustomObtainAuthToken.as_view())
]
