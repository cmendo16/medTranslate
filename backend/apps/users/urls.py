from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, SignupView

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', SignupView.as_view(), name='signup'),

]
