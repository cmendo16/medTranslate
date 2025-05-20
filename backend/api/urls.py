from django.urls import path, include 
from rest_framework.routers import DefaultRouter 
from .views import CategoryViewSet, PhraseViewSet, ProfileViewSet, FavoriteViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'phrases', PhraseViewSet, basename='phrase')
router.register(r'favorites', FavoriteViewSet, basename='favorite')
router.register(r'profiles', ProfileViewSet, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]