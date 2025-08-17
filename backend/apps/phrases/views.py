from .permissions import IsOwnerOrDefaultReadOnly
from .models import Phrase
from .serializers import PhraseSerializer
from rest_framework import permissions, viewsets
from rest_framework.exceptions import PermissionDenied, ValidationError
from django.db.models import Q

# Create your views here.
class PhraseViewSet(viewsets.ModelViewSet): 
    serializer_class = PhraseSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrDefaultReadOnly]
    
    def get_queryset(self):
        user = self.request.user
        return Phrase.objects.filter(Q(is_default=True) | Q(added_by=user)).select_related("category")

    def perform_create(self, serializer): 
        serializer.save(added_by=self.request.user, is_default=False)
        
    def perform_update(self, serializer): 
        instance = self.get_object()
        
        if instance.is_default: 
            raise PermissionDenied("Default phrases cannot be edited.")
        
        serializer.save()
        
    def perform_destroy(self, instance): 
        if instance.is_default: 
            raise ValidationError("Default phrases cannot be deleted.")
        instance.delete()