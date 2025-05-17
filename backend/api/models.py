from django.db import models
from django.conf import settings 

# Create your models here.

# This model allows for a 2 level hierarchy 
# the top level Medication and Symptoms, each having subcategories 
class Category(models.Model):
    MEDICATION = 'med' 
    SYMPTOM = 'sym'
    
    TYPE_CHOICES = [
        (MEDICATION, 'Medication'), 
        (SYMPTOM, 'Symptom'),
    ]
    
    name = models.CharField(max_length=100)
    
    type = models.CharField(max_length=3, choices=TYPE_CHOICES)
    
    # if parent is null, then it's a top level category
    parent = models.ForeignKey(
        'self', 
        null=True, 
        blank=True,
        related_name='subcategories', 
        on_delete=models.CASCADE
    )
    
    order = models.PositiveBigIntegerField(default=0)
    
    class Meta: 
        ordering =['type', 'order', 'name']
        
def __str__(self):
        # e.g. “Medications → Analgesics” for a subcategory
        return (
            f"{self.parent.name} → {self.name}"
            if self.parent else
            self.name
        )

class Phrase(models.Model):
    
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE,
        related_name='phrases'
    )
    
    text_original = models.CharField(max_length=100)
    text_translation = models.CharField(max_length=100)
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, # how do i get the user here? lol
        on_delete=models.SET_NULL,
        null=True, 
        related_name='added_phrases'
    )
    
    class Meta: 
        unique_together = ('category', 'text_original')
        ordering = ['text_original']
        
    def __str__(self):
         return f"{self.text_original} → {self.text_translation}"
        
class Favorite(models.Model): 
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, # Again, find where you put this value in settings?
        on_delete=models.CASCADE, 
        related_name='favorites'
    )    
    
    phrase = models.ForeignKey(
        Phrase,
        on_delete=models.CASCADE, 
        related_name='favorited_by'
    )

class Profile(models.Model):
    PATIENT = 'patient'
    PROFESSIONAL = 'professional'
    
    MODE_CHOICES = [
        (PATIENT, 'Patient'), 
        (PROFESSIONAL, 'Professional')
    ]
    
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='profile'
    )
    
    mode = models.CharField(
        max_length=12,
        choices=MODE_CHOICES,
        default=PATIENT
    )
    
    preferred_language = models.CharField(
        max_length=10, 
        default='es', 
        help_text="e.g. 'es' for Spanish "
    )
    
def __str__(self):
    return f"{self.user.username}'s profile"


    
