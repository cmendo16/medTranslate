from django.conf import settings
from django.db import models
from apps.phrases.models import Phrase

# Create your models here.
class Favorite(models.Model): 
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='favorites'
    )    
    
    phrase = models.ForeignKey(
        Phrase,
        on_delete=models.CASCADE, 
        related_name='favorited_by'
    )
    created_at = models.DateTimeField(
        auto_now_add = True
    )
    
    class Meta: 
        unique_together = ('user', 'phrase')
        ordering = ['-created_at']
        
    def __str__(self):
        return f"{self.user.username} ❤️ {self.phrase.text_original}"
