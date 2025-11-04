from rest_framework import serializers
from apps.products.models import ProductsModel


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsModel
        exclude = ['created_at', 'updated_at', 'uuid']
        read_only_fields = ['real_price']