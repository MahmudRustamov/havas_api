from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from apps.products.models import ProductsModel
from apps.shared.models import BaseModel


class RecipeModel(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    media_files = GenericRelation('shared.Media',related_query_name='recipes')
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    steps = models.TextField()
    cook_time = models.CharField(max_length=50)
    calories = models.PositiveIntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)

    def __str__(self):
        return self.title


class RecipeIngredient(BaseModel):
    recipe = models.ForeignKey(RecipeModel, on_delete=models.CASCADE, related_name='ingredients')
    product = models.ForeignKey(ProductsModel, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100)
    is_optional = models.BooleanField(default=False)

    def __str__(self):
        return self.product.title
