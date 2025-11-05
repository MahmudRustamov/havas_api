from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models.user import VerificationCode, User
from apps.users.serializers.register import RegisterSerializer, VerifyLoginCodeSerializer, RequestLoginCodeSerializer


class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({'detail': 'Verification code sent to email'}, status=status.HTTP_201_CREATED)


class VerifyEmailAPIView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    @staticmethod
    def post(request):
        email = request.data.get('email')
        code = request.data.get('code')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=400)

        try:
            verification = VerificationCode.objects.filter(user=user, code=code, used=False).latest('created_at')
        except VerificationCode.DoesNotExist:
            return Response({'error': 'Invalid or expired code'}, status=400)

        if not verification.is_valid():
            return Response({'error': 'Code expired'}, status=400)

        user.is_active = True
        user.save()
        verification.used = True
        verification.save()

        return Response({'detail': 'Email verified successfully.'})

class RequestLoginCodeAPIView(generics.CreateAPIView):
    serializer_class = RequestLoginCodeSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"detail": "Verification code sent to your email."},
            status=status.HTTP_200_OK
        )


class VerifyLoginCodeAPIView(generics.CreateAPIView):
    serializer_class = VerifyLoginCodeSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]

        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "detail": "Login successful"
        }, status=status.HTTP_200_OK)