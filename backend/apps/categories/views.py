from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import Category
from .serializers import CategorySerializer

# Create your views here.
class CategoryViewSet(viewsets.ReadOnlyModelViewSet): 
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    