from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions
from apps.recipe.models import RecipeModel


@register(RecipeModel)
class RecipeTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)