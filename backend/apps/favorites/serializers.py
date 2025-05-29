from backend.apps.favorites.models import Favorite
from rest_framework import serializers

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Favorite
        fields = ('id','user','phrase','created_at')
