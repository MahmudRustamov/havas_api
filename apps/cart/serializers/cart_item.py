from rest_framework import serializers
from apps.cart.models import CartList, CartItem

from rest_framework import serializers
from apps.cart.models import CartItem, ProductsModel


class CartItemSerializer(serializers.ModelSerializer):
    # Productni oddiy raqam (Integer) sifatida olish
    product = serializers.IntegerField(required=False, allow_null=True)
    title = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = [
            'id',
            'shopping_list',
            'product',
            'title',
            'custom_title',
            'quantity',
            'measurement',
            'is_checked'
        ]

    def get_title(self, obj):
        if obj.product:
            return obj.product.title
        return None

    def validate(self, data):
        product_id = data.get('product')
        custom_title = data.get('custom_title')

        # product raqam kiritilgan bo‘lsa, tekshiramiz
        if product_id:
            try:
                product = ProductsModel.objects.get(pk=product_id)
                data['product'] = product
            except ProductsModel.DoesNotExist:
                data['product'] = None

        # product ham custom_title ham yo‘q bo‘lsa — xato
        if not data.get('product') and not custom_title:
            raise serializers.ValidationError({
                "non_field_error": "Mahsulot yoki custom_title kiritilishi kerak."
            })

        # Agar product bor bo‘lsa, custom_title ni olib tashlaymiz
        if data.get('product'):
            data['custom_title'] = None

        return data

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        # Agar product bo‘lsa, custom_title’ni ko‘rsatmaymiz
        if instance.product:
            rep.pop('custom_title', None)
        else:
            rep.pop('product', None)
            rep.pop('title', None)

        return rep



class CartListSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = CartList
        fields = ['id', 'name', 'color', 'items']

    def create(self, validated_data):
        user = self.context['request'].user
        return CartList.objects.create(user=user, **validated_data)