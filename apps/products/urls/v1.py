from django.urls import path

from apps.users.views.device import DeviceRegisterCreateAPIView, DeviceListApiView

app_name = 'products'

urlpatterns = [
    path('product/', DeviceRegisterCreateAPIView.as_view(), name='create'),
]
