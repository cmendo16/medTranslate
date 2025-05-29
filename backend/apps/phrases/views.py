from django.shortcuts import render

from .models import Phrase
from .serializers import PhraseSerializer
from rest_framework import permissions, viewsets

# Create your views here.
class PhraseViewSet(viewsets.ModelViewSet): 
    queryset = Phrase.objects.all()
    serializer_class = PhraseSerializer
    permission_classes = [permissions.IsAuthenticated]
    