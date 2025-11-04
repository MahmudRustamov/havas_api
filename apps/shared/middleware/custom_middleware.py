import jwt
from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.tokens import AccessToken
from apps.users.models.device import Device


class DeviceDetectMiddleware(MiddlewareMixin):
    @staticmethod
    def process_request(request):
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        request.custom_user_id = None
        request.device_type = None
        request.device_model = None
        request.user_language = None

        if not auth_header.startswith('Bearer '):
            return

        token = auth_header.split(' ')[1]

        try:
            access_token = AccessToken(token)
            user_id = access_token.get('user_id')
            request.custom_user_id = user_id

            device = (
                Device.objects
                .filter(user_id=user_id, is_active=True)
                .order_by('-last_login')
                .first()
            )

            if device:
                request.device_type = device.device_type
                request.device_model = device.device_mode
                request.user_language = device.language

        except jwt.ExpiredSignatureError:
            pass
