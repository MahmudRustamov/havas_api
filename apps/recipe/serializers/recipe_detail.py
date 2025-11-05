from rest_framework import serializers

from apps.recipe.models import RecipeModel
from apps.recipe.serializers.recipe_list_create import RecipeIngredientWriteSerializer, RecipeTranslationMixin
from apps.shared.mixins.translation_mixins import TranslatedFieldsReadMixin


class RecipeDetailSerializer(RecipeTranslationMixin,TranslatedFieldsReadMixin,serializers.ModelSerializer):
    ingredients = RecipeIngredientWriteSerializer(many=True, read_only=True)

    class Meta:
        model = RecipeModel
        fields = [
            'id', 'title', 'description', 'image', 'video_url',
            'steps', 'cook_time', 'calories', 'rating', 'ingredients'
        ]


