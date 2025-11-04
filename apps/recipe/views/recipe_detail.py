from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.recipe.models import RecipeModel
from apps.recipe.serializers.recipe_detail import RecipeDetailSerializer
from apps.shared.utils.custom_response import CustomResponse


class RecipeDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def get(request, pk, *args, **kwargs):
        try:
            recipe = RecipeModel.objects.get(pk=pk)
        except RecipeModel.DoesNotExist:
            return CustomResponse.error(message_key='NOT_FOUND', status=status.HTTP_200_OK)

        serializer = RecipeDetailSerializer(recipe)
        return CustomResponse.success(
            message_key="SUCCESS_MESSAGE",
            data=serializer.data
        )
