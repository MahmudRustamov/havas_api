from rest_framework import serializers
from apps.products.models import ProductsModel
from apps.products.serializers.product_create import ProductTranslationMixin
from apps.shared.mixins.translation_mixins import TranslatedFieldsReadMixin


class ProductDetailSerializer(ProductTranslationMixin, TranslatedFieldsReadMixin, serializers.ModelSerializer):
    class Meta:
        model = ProductsModel
        fields = ['id', 'uuid', 'title', 'description',
                  'price', 'real_price', 'measurement',
                  'created_at', 'is_active', 'category', 'discount']