from django.contrib.auth import authenticate
from rest_framework import serializers

from apps.users.models.user import VerificationCode, User
from apps.users.utils.code_generators import generate_unique_username, generate_secure_password, \
    generate_verification_code, send_email


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','phone_number','username']


    def create(self, validated_data):
        data = {
            'email': validated_data['email'],
            'phone_number': validated_data['phone_number'],
            'username': generate_unique_username(),
            'password': generate_secure_password(),
            'is_active': False
        }
        user = User.objects.create_user(**data)
        code = generate_verification_code()
        send_email(receiver_email=validated_data['email'], body=code)
        VerificationCode.objects.create(user=user, code=code)

        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self,attrs):
        credentials = {
            "phone_number":attrs.get('phone_number'),
            "code": attrs.get('code'),
        }

        user = authenticate(request=self.context['request'], **credentials)
        if user is None:
            raise serializers.ValidationError("Email or verification code is incorrect")
        else:
            attrs['user'] = user
            return attrs


class ProfileRetrieveSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    rentals_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id','email','username','full_name','rentals_count']

    @staticmethod
    def get_full_name(obj):
        return f"{obj.first_name} {obj.last_name}".strip()

    @staticmethod
    def get_rentals_count(obj):
        return obj.rentals.count()
