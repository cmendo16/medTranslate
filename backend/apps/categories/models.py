from django.db import models
from django.conf import settings 

# Create your models here.
class Category(models.Model):
    MEDICATION = 'med' 
    SYMPTOM = 'sym'
    COMMON_SIGS = 'sig'
    
    TYPE_CHOICES = [
        (MEDICATION, 'Medication'), 
        (SYMPTOM, 'Symptom'),
        (COMMON_SIGS, 'Common Sigs')
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
        return (
            f"{self.parent.name} → {self.name}"
            if self.parent else
            self.name
        )
