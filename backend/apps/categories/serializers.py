from ..categories.models import Category
from rest_framework import serializers



class CategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.SerializerMethodField()
    class Meta:
        model  = Category
        fields = ("id", "name", "type", "parent", "order", "subcategories")

    def get_subcategories(self, obj):
        # only populate when the object is a top‑level node
        if obj.parent_id is None:
            qs = obj.subcategories.all().order_by("order", "name")
            return CategorySerializer(qs, many=True, context=self.context).data
        return []