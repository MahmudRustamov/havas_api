from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import PermissionDenied

from apps.recipe.models import RecipeModel, RecipeIngredient
from apps.recipe.serializers.recipe_detail import RecipeDetailSerializer
from apps.recipe.serializers.recipe_list_create import RecipeCreateSerializer, RecipeIngredientWriteSerializer, \
    RecipeListSerializer
from apps.shared.permissions.mobile import IsMobileOrWebUser
from apps.shared.utils.custom_response import CustomResponse


class RecipeListCreateAPIView(ListCreateAPIView):
    queryset = RecipeModel.objects.all()
    serializer_class = RecipeCreateSerializer
    permission_classes = [IsAuthenticated]


    def get_serializer_class(self):
        if self.request.method == "POST":
            return RecipeCreateSerializer
        elif self.request.method == "GET" and self.request.device_type == "WEB":
            return RecipeListSerializer
        else:
            return RecipeDetailSerializer

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

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().order_by('-id'))
        print(request.lang, request.device_type, "********")
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True, context={'request': request})
            return CustomResponse.success(
                message_key="SUCCESS_MESSAGE",
                data=serializer.data,
                status_code=status.HTTP_200_OK,
                request=request
            )

        serializer = self.get_serializer(queryset, many=True, context={'request': request})
        return CustomResponse.success(
            message_key="SUCCESS_MESSAGE",
            data=serializer.data,
            status_code=status.HTTP_200_OK,
            request=request
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