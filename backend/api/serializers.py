from rest_framework import serializers
from .models import Category, Favorite, Phrase, Profile

class CategorySerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Category
        fields = ('id', 'name', 'type', 'parent', 'order',)
        
class PhraseSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Phrase
        fields = ('id', 'text_original', 'text_translation', 'category', 'added_by')
        
class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Favorite
        fields = ('id','user','phrase','created_at')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Profile
        fields = ('user','mode','preferred_language')