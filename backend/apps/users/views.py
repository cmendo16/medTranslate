from rest_framework import permissions, viewsets, generics, throttling
from .serializers import ProfileSerializer, SignupSerializer
from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model()   
class MyProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class   = ProfileSerializer

    def get_object(self):
        return self.request.user.profile # type: ignore

class SignupView(generics.CreateAPIView): 
    serializer_class = SignupSerializer

    permission_classes = [permissions.AllowAny]
    throttle_classes   = [throttling.UserRateThrottle]
     