from rest_framework import permissions, viewsets, generics, throttling
from .models import Profile
from .serializers import ProfileSerializer, SignupSerializer
from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model()   
class MyProfileView(generics.RetrieveUpdateDestroyAPIView): 
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self): 
        return self.request.user.profile # type: ignore
    
class SignupView(generics.CreateAPIView): 
    serializer_class = SignupSerializer
    # allow any user to sign up 
    permission_classes = [permissions.AllowAny]
    throttle_classes   = [throttling.UserRateThrottle]
     