from django.shortcuts import render
# Favorites view for getting, creating and deleting favorite phrases 

from .models import Favorite
from .serializers import  FavoriteSerializer
from rest_framework import permissions, viewsets, status
from rest_framework.decorators import action 
from rest_framework.response import Response
# Create your views here.

class FavoriteViewSet(viewsets.GenericViewSet):
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    # get the favorites of the current user
    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)
    
    # list the favorites of the user 
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # POST endpoint to toggle (add/remove) favorites 
    @action(detail=False, methods=['post'])
    def toggle(self, request):
        phrase_id = request.data.get('phrase_id')
        
        if not phrase_id:
            return Response({'detail': 'phrase_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        # create favorite if it doesn't exist 
        favorite, created = Favorite.objects.get_or_create(
            user=request.user,
            phrase_id = phrase_id
        )
        
        if not created: 
            favorite.delete()
            return Response({'favorited': False})
        
        return Response({'favorited': True})