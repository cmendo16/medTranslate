from django.contrib import admin

from ..categories.models import Category

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "parent", "order")
    list_filter = ('type',)
    search_fields = ('name',)
    