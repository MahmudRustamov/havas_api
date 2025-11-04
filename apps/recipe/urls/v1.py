from django.urls import path

from apps.recipe.views.recipe_create import RecipeListCreateAPIView, RecipeIngredientListCreateAPIView
from apps.recipe.views.recipe_detail import RecipeDetailAPIView

app_name = 'recipe'
urlpatterns = [
    path('', RecipeListCreateAPIView.as_view(), name='recipe-create'),
    path('<int:pk>/', RecipeDetailAPIView.as_view(), name='recipe-detail'),
]
