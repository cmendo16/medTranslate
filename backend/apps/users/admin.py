from django.contrib import admin
from .models import Category, Phrase, Favorite, Profile

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "parent", "order")
    list_filter = ('type',)
    search_fields = ('name',)
    
@admin.register(Phrase)
class PhraseAdmin(admin.ModelAdmin):
    list_display = ("text_original", "text_translation", "category", "added_by")
    list_filter = ("category__type",)
    search_fields = ("text_original", "text_translation",)
    
@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ("user", "phrase", "created_at",)
    search_fields = ("user__username",)
    
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin): 
    list_display = ("user", "mode", "preferred_language",)
    search_fields = ("mode", "preferred_language",)
    
    
    