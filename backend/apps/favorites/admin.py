from django.contrib import admin
from ..favorites.models import Favorite

# Register your models here.
@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ("user", "phrase", "created_at",)
    search_fields = ("user__username",)
    