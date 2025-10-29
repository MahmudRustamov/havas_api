
from rest_framework import serializers
from .models import ProductsModel, CategoryModel


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['id', 'title', 'created_at']



class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = ProductsModel
        fields = [
            'id', 'name', 'image', 'price', 'weight',
            'description', 'stock', 'rating', 'category', 'created_at'
        ]
