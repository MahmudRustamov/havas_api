from rest_framework import serializers
from apps.products.models import ProductsModel
from apps.recipe.models import RecipeIngredient, RecipeModel

from apps.shared.mixins.translation_mixins import (
    TranslatedFieldsWriteMixin,
    TranslatedFieldsReadMixin
)


class RecipeTranslationMixin:
    """Shared configuration for OnBoarding serializers"""
    translatable_fields = ['title', 'description', 'images']
    media_fields = ['images']


class RecipeIngredientWriteSerializer(TranslatedFieldsWriteMixin,serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=ProductsModel.objects.all())

    class Meta:
        model = RecipeIngredient
        fields = ['product', 'quantity', 'is_optional']


class RecipeCreateSerializer(TranslatedFieldsWriteMixin,serializers.ModelSerializer):
    ingredients = serializers.ListField(
        write_only=True,
        child=serializers.DictField(),
        required=False
    )

    class Meta:
        model = RecipeModel
        fields = [
            'id', 'title', 'description', 'image', 'video_url',
            'steps', 'cook_time', 'calories', 'rating', 'ingredients'
        ]

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients', [])
        recipe = RecipeModel.objects.create(**validated_data)

        for item in ingredients_data:
            product_id = item.get('product')
            if not product_id:
                raise serializers.ValidationError("Ingredient must have a product_id")

            try:
                product_instance = ProductsModel.objects.get(id=product_id)
            except ProductsModel.DoesNotExist:
                raise serializers.ValidationError(f"Product with id {product_id} does not exist")

            RecipeIngredient.objects.create(
                recipe=recipe,
                product=product_instance,
                quantity=item.get('quantity', ''),
                is_optional=item.get('is_optional', False)
            )

        return recipe
