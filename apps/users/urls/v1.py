from django.urls import path

from apps.users.views.auth import RegisterView, VerifyEmailAPIView, RequestLoginCodeAPIView, VerifyLoginCodeAPIView
from apps.users.views.device import DeviceRegisterCreateAPIView, DeviceListApiView

app_name = 'users'

urlpatterns = [
    path('devices/', DeviceRegisterCreateAPIView.as_view(), name='device-register'),
    path('devices/list/', DeviceListApiView.as_view(), name='device-list'),
    path('register/', RegisterView.as_view(), name='register'),
    path('verify-email/', VerifyEmailAPIView.as_view(), name='verify-email'),
    path('login/', RequestLoginCodeAPIView.as_view(), name='login'),
    path('login/verify-code/', VerifyLoginCodeAPIView.as_view(), name='verify-login-code'),
    # path('logout/', LogoutAPIView.as_view(), name='logout'),
    # path('profile/', ProfileRetrieveAPIView.as_view(), name='profile'),
]
