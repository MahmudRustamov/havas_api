from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import PermissionDenied

from apps.recipe.models import RecipeModel, RecipeIngredient
from apps.recipe.serializers.recipe_detail import RecipeDetailSerializer
from apps.recipe.serializers.recipe_list_create import RecipeCreateSerializer, RecipeIngredientWriteSerializer
from apps.shared.utils.custom_response import CustomResponse


class RecipeListCreateAPIView(ListCreateAPIView):
    queryset = RecipeModel.objects.all()
    serializer_class = RecipeCreateSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied("You are not allowed to create a recipe")

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            recipe = serializer.save()
            return CustomResponse.success(
                message_key="SUCCESS_MESSAGE",
                data=RecipeDetailSerializer(recipe).data,
                status_code=status.HTTP_201_CREATED
            )
        return CustomResponse.error(
            message_key="VALIDATION_ERROR",
            errors=serializer.errors
        )


class RecipeIngredientListCreateAPIView(ListCreateAPIView):
    queryset = RecipeIngredient.objects.all()
    serializer_class = RecipeIngredientWriteSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied("You are not allowed to add ingredients")

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            ingredient = serializer.save()
            return CustomResponse.success(
                message_key="SUCCESS_MESSAGE",
                data=serializer.data,
                status_code=status.HTTP_201_CREATED
            )
        return CustomResponse.error(
            message_key="VALIDATION_ERROR",
            errors=serializer.errors
        )