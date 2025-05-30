from rest_framework import serializers
from ..phrases.models import Phrase

class PhraseSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Phrase
        fields = ('id', 'text_original', 'text_translation', 'category', 'added_by')
       