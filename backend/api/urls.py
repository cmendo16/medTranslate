from django.urls import path, include 
from rest_framework.routers import DefaultRouter 
from .views import CategoryViewSet, PhraseViewSet, ProfileViewSet, FavoriteViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'phrases', PhraseViewSet, basename='phrase')
router.register(r'favorites', FavoriteViewSet, basename='favorite')
router.register(r'profiles', ProfileViewSet, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
]