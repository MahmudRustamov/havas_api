from datetime import timedelta
from django.utils import timezone
from rest_framework import serializers
from apps.users.models.user import User, VerificationCode
from apps.users.utils.code_generators import (
    generate_unique_username,
    generate_secure_password,
    generate_verification_code,
    send_email
)


class RegisterSerializer(serializers.ModelSerializer):
    """User registration with email verification code"""

    class Meta:
        model = User
        fields = ['email', 'phone_number']

    def validate(self, attrs):
        email = attrs.get('email')
        phone = attrs.get('phone_number')

        if not email and not phone:
            raise serializers.ValidationError("Email or phone number is required")

        if email and User.objects.filter(email=email).exists():
            raise serializers.ValidationError("This email is already registered")

        if phone and User.objects.filter(phone_number=phone).exists():
            raise serializers.ValidationError("This phone number is already registered")

        return attrs

    def create(self, validated_data):
        email = validated_data.get('email')
        phone = validated_data.get('phone_number')

        user = User.objects.create_user(
            email=email,
            phone_number=phone,
            username=generate_unique_username(),
            password=generate_secure_password(),
            is_active=False
        )

        # Generate and send verification code
        code = generate_verification_code()
        VerificationCode.objects.create(user=user, code=code)
        if email:
            send_email(receiver_email=email, body=f"Your verification code: {code}")

        return user


class VerifyCodeSerializer(serializers.Serializer):
    """Check verification code and activate user"""
    email = serializers.EmailField()
    code = serializers.CharField(max_length=6)

    def validate(self, attrs):
        email = attrs.get("email")
        code = attrs.get("code")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found")

        try:
            verification = VerificationCode.objects.filter(user=user, code=code, used=False).latest("created_at")
        except VerificationCode.DoesNotExist:
            raise serializers.ValidationError("Invalid or expired code")

        if not verification.is_valid():
            raise serializers.ValidationError("Verification code is expired")

        verification.used = True
        verification.save()
        user.is_active = True
        user.is_email_verified = True
        user.save()

        attrs["user"] = user
        return attrs


class RequestLoginCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()

    @staticmethod
    def validate_email(value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("User with this email does not exist.")
        return value

    def create(self, validated_data):
        user = User.objects.get(email=validated_data['email'])
        code = generate_verification_code()
        VerificationCode.objects.create(user=user, code=code)
        send_email(receiver_email=user.email, body=f"Your verification code: {code}")
        return user


class VerifyLoginCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=6)

    def validate(self, attrs):
        email = attrs.get("email")
        code = attrs.get("code")

        try:
            user = User.objects.get(email=email)
            vcode = VerificationCode.objects.filter(user=user, code=code).latest("created_at")
        except (User.DoesNotExist, VerificationCode.DoesNotExist):
            raise serializers.ValidationError("Invalid email or code.")

        if (timezone.now() - vcode.created_at) > timedelta(minutes=15):
            raise serializers.ValidationError("Verification code expired.")

        if vcode.used:
            raise serializers.ValidationError("This code has already been used.")

        attrs["user"] = user
        return attrs