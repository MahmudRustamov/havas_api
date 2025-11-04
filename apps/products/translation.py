from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from apps.products.models import ProductsModel


@register(ProductsModel)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)