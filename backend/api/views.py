from rest_framework import permissions, viewsets, generics, throttling
from .models import Category, Favorite, Phrase, Profile
from .serializers import CategorySerializer, FavoriteSerializer, PhraseSerializer, ProfileSerializer, SignupSerializer
from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model()

class CategoryViewSet(viewsets.ReadOnlyModelViewSet): 
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    
class FavoriteViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
class PhraseViewSet(viewsets.ModelViewSet): 
    queryset = Phrase.objects.all()
    serializer_class = PhraseSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class ProfileViewSet(viewsets.ReadOnlyModelViewSet): 
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class SignupView(generics.CreateAPIView): 
    serializer_class = SignupSerializer
    # allow any user to sign up 
    permission_classes = [permissions.AllowAny]
    throttle_classes   = [throttling.UserRateThrottle]
    