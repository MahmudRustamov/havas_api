from django.db.models.signals import pre_save
from django.dispatch import receiver

from apps.products.models import ProductsModel


@receiver(pre_save, sender=ProductsModel)
def update_price(sender, instance, **kwargs):
    try:
        if instance.price is not None and instance.discount is not None:
            instance.real_price = instance.price - (instance.price * instance.discount / 100)
    except Exception as e:
        return e
