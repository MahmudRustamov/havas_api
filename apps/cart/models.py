from django.contrib.auth import get_user_model
from django.db import models
from apps.products.models import ProductsModel
from apps.shared.models import BaseModel


User = get_user_model()


class CustomMeasurement(models.TextChoices):
    GR = "GR", "Gram"
    PC = "PC", "Piece"
    L = "L", 'Litre'



class CartList(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart_lists")
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=15, default='#ffffff')

    def __str__(self):
        return f"{self.name} ({self.user.username})"

    class Meta:
        verbose_name = "Cart List"
        verbose_name_plural = "Cart Lists"


class CartItem(BaseModel):
    shopping_list = models.ForeignKey(CartList, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(ProductsModel, on_delete=models.SET_NULL, null=True, blank=True, related_name='shopping_items')

    custom_title = models.CharField(max_length=128, null=True, blank=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    measurement = models.CharField(choices=CustomMeasurement, default=CustomMeasurement.GR)
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.product.title if self.product else self.custom_title

    class Meta:
        verbose_name = 'Cart Item'
        verbose_name_plural = 'Cart Items'


