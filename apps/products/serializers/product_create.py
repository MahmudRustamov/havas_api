
from rest_framework import serializers

from apps.products.models import ProductsModel
from apps.shared.mixins.translation_mixins import (
    TranslatedFieldsWriteMixin,
    TranslatedFieldsReadMixin
)


class ProductTranslationMixin:
    """Shared configuration for OnBoarding serializers"""
    translatable_fields = ['title', 'description', 'images']
    media_fields = ['images']


class ProductCreateSerializer(TranslatedFieldsWriteMixin, serializers.ModelSerializer):
    real_price = serializers.DecimalField(required=False, max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = ProductsModel
        fields = [
            'title_en', 'title_uz',
            'description_en', 'description_uz',
            'price', 'real_price',
            'measurement',
            'is_active', 'category', 'discount',
            'image'
        ]


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsModel
        exclude = ['title', 'description']


class ProductDetailSerializer(ProductTranslationMixin, TranslatedFieldsReadMixin, serializers.ModelSerializer):
    class Meta:
        model = ProductsModel
        fields = ['id', 'uuid', 'title', 'description',
                  'price', 'real_price', 'measurement',
                  'created_at', 'is_active', 'category', 'discount']
