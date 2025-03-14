from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    vendor_name = serializers.CharField(source="vendor.business_name", read_only=True)

    class Meta:
        model = Product
        fields = ["id", "vendor", "vendor_name", "name", "description", "price", "stock", "created_at"]
        extra_kwargs = {"vendor": {"read_only": True}}
