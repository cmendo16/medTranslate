from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import Category
from .serializers import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    
    queryset         = Category.objects.all().select_related("parent")
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:  
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]