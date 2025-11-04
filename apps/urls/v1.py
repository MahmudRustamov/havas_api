from django.urls import path, include

urlpatterns = [
    path('users/', include('apps.users.urls.v1', namespace='users')),
    path('products/', include('apps.products.urls.v1', namespace='products')),
    # path('stories/', include('apps.stories.urls.v1', namespace='stories')),
    path('recipes/', include('apps.recipe.urls.v1', namespace='recipe')),
    path('stories/', include('apps.stories.urls.v1', namespace='stories')),
    path('cart/', include('apps.cart.urls.v1', namespace='cart')),
]
