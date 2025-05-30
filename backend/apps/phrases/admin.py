from django.contrib import admin
from ..phrases.models import Phrase

# Register your models here.

@admin.register(Phrase)
class PhraseAdmin(admin.ModelAdmin):
    list_display = ("text_original", "text_translation", "category", "added_by")
    list_filter = ("category__type",)
    search_fields = ("text_original", "text_translation",)
    