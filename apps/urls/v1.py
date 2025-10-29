from django.urls import path, include

urlpatterns = [
    path('users/', include('apps.users.urls.v1', namespace='users')),
    path('products/', include('apps.products.urls.v1', namespace='products'))
]
