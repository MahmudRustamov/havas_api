from rest_framework import status
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.products.models import ProductsModel
from apps.products.serializers import ProductSerializer


class ProductCreateView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductListAPIView(APIView):
    def get(self, request):
        products = ProductsModel.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


