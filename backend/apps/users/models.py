from django.db import models
from django.conf import settings 

# Create your models here.

# This model allows for a 2 level hierarchy 
# the top level Medication and Symptoms, each having subcategories 
 
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
    
