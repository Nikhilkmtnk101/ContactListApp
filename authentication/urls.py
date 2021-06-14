from django.urls import path
from .views import UserRegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/',UserRegisterView.as_view(),name='user-register'),
    path('login/',TokenObtainPairView.as_view(),name='user-login'),
    path('refresh-token/',TokenRefreshView.as_view(),name='refresh-token'),
]