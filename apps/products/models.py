from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from apps.shared.models import BaseModel


class Measurement(models.TextChoices):
    GR = "GR", "Gram"
    PC = "PC", "Piece"
    L = "L", 'Litre'

class ProductCategory(models.TextChoices):
    BREAKFAST = "BREAKFAST", "Breakfast"
    LUNCH = "LUNCH", "Lunch"
    DINNER = "DINNER", "Dinner"
    ALL = "ALL", "All"



class ProductsModel(BaseModel):
    media_files = GenericRelation('shared.Media',related_query_name='products')
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    title = models.CharField(max_length=128,db_index=True)
    description = models.TextField(blank=True)

    discount = models.PositiveSmallIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    real_price = models.DecimalField(max_digits=10, decimal_places=2)

    category = models.CharField(
        choices=ProductCategory, default=ProductCategory.ALL,
        db_index=True
    )
    measurement = models.CharField(
        choices=Measurement, default=Measurement.GR
    )

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'