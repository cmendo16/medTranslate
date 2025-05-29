from django.shortcuts import render

# Create your views here.
from .models import Favorite
from .serializers import  FavoriteSerializer
from rest_framework import permissions, viewsets
# Create your views here.

class FavoriteViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    