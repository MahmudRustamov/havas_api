from django.urls import path

from apps.products.views.product_detail import ProductDetailApiView
from apps.products.views.product_lis_create import ProductListCreateApiView

app_name = 'products'

urlpatterns = [
    path('', ProductListCreateApiView.as_view(), name='list-create'),
    path('<int:pk>/', ProductDetailApiView.as_view(), name='detail'),
]
