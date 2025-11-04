from rest_framework import generics, permissions
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from apps.cart.models import CartItem, CartList
from apps.cart.serializers.cart_item import CartItemSerializer, CartListSerializer


class CartListDetail(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CartListSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return CartList.objects.filter(user=self.request.user)


class CartItemCreateAPIView(generics.CreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class CartItemUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(shopping_list__user=self.request.user)