from django.db import models
from apps.shared.models import BaseModel


class CategoryModel(BaseModel):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title


class ProductsModel(BaseModel):
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    name = models.CharField(max_length=128)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='products')
    stock = models.PositiveIntegerField(blank=True, null=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    def __str__(self):
        return self.name


