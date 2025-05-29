from django.conf import settings
from django.db import models
from backend.apps.categories.models import Category

# Create your models here.
class Phrase(models.Model):
    
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE,
        related_name='phrases'
    )
    
    text_original = models.CharField(max_length=100)
    text_translation = models.CharField(max_length=100)
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL,
        null=True, 
        related_name='added_phrases'
    )
    
    class Meta: 
        unique_together = ('category', 'text_original')
        ordering = ['text_original']
        
    def __str__(self):
         return f"{self.text_original} → {self.text_translation}"
        