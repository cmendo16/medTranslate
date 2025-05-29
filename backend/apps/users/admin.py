from django.contrib import admin
from .models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin): 
    list_display = ("user", "mode", "preferred_language",)
    search_fields = ("mode", "preferred_language",)
    
    
    