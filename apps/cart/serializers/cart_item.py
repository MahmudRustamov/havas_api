from rest_framework import serializers
from apps.cart.models import CartList, CartItem

class CartItemSerializer(serializers.ModelSerializer):
    product_title = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['id', 'shopping_list', 'product', 'product_title', 'custom_title', 'quantity', 'measurement', 'is_checked']

    def get_product_title(self, obj):
        return obj.product.title if obj.product else None

    def validate(self, data):
        product = data.get('product')
        custom_title = data.get('custom_title')

        if not product and not custom_title:
            raise serializers.ValidationError({
                "non_field_error": "Either 'product' or 'custom_title' must be provided."
            })

        if product and custom_title:
            data['custom_title'] = None

        return data


class CartListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartList
        fields = ['name', 'color']

    def create(self, validated_data):
        user = self.context['request'].user
        return CartList.objects.create(user=user, **validated_data)
