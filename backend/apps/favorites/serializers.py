from .models import Favorite
from rest_framework import serializers
from ..phrases.models import Phrase

class FavoritePhraseSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Phrase
        fields = ("text_original", "text_translation")
class FavoriteSerializer(serializers.ModelSerializer):
    
    favorite_phrase = FavoritePhraseSerializer(read_only=True, source ="phrase")
    
    phrase_id = serializers.PrimaryKeyRelatedField(
        queryset=Phrase.objects.all(),
        write_only=True,
        source="phrase",
    )
    class Meta:
        model  = Favorite
        fields = ['id', 'favorite_phrase', 'phrase_id', 'created_at'
        ]
