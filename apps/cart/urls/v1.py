from django.urls import path
from apps.cart.views.cart_detail import CartItemCreateAPIView, CartItemUpdateDeleteAPIView, CartListDetail
from apps.cart.views.cart_list import CartListCreateAPIView

app_name = 'cart'

urlpatterns = [
    path('lists/', CartListCreateAPIView.as_view(), name='cart-list-create'),
    path('lists/<int:id>/', CartListDetail.as_view(), name='detail'),
    path('items/', CartItemCreateAPIView.as_view(), name='cart-item-create'),
    path('items/<int:pk>/', CartItemUpdateDeleteAPIView.as_view(), name='cart-item-detail'),
]