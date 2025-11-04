from rest_framework import status
from rest_framework.reverse import reverse_lazy
from rest_framework.test import APITestCase

from apps.users.models.device import AppVersion, DeviceType, Device


class DeviceRegisterApiTestCase(APITestCase):
    def setUp(self):
        """Set up test data"""
        self.url = reverse_lazy('users:device-register')
        self.app_version = AppVersion.objects.create(
            version="1.0.0",
            force_update=False,
            device_type=DeviceType.ALL,
            is_active=True
        )
        self.base_payload = {
            "device_model": "iPhone 15 Pro",
            "operation_version": "iOS 18.1",
            "device_type": "IOS",
            "device_id": "F2B5E1C8-1C44-4F9D-9B99-ABF0D1C021212",
            "ip_address": "45.85.12.101",
            "language": "EN",
            "theme": "LIGHT",
            "app_version": self.app_version.id,
            "firebase_token": "fcm_token_12345_ios_examp12121"
        }

    # def test_device_register_success(self):
    #     """Test successful device registration"""
    #     response = self.client.post(path=self.url, data=self.base_payload)
    #
    #     self.assertEqual(status.HTTP_201_CREATED, response.status_code)
    #     self.assertIn('device_token', response.json().get('data'))
    #     self.assertTrue(Device.objects.filter(device_id=self.base_payload['device_id']).exists())
    #
    # def test_device_register_android_success(self):
    #     """Test successful Android device registration"""
    #     payload = self.base_payload.copy()
    #     payload.update({
    #         "device_model": "Samsung Galaxy S24",
    #         "operation_version": "Android 14",
    #         "device_type": "ANDROID",
    #         "device_id": "android-unique-id-12345",
    #         "firebase_token": "fcm_token_android_example"
    #     })
    #
    #     response = self.client.post(path=self.url, data=payload)
    #
    #     self.assertEqual(status.HTTP_201_CREATED, response.status_code)
    #     self.assertIn('device_token', response.json().get('data'))
    #
    # def test_device_register_missing_required_field(self):
    #     """Test registration fails when required field is missing"""
    #     required_fields = ['device_model', 'device_type', 'device_id', 'app_version']
    #
    #     for field in required_fields:
    #         payload = self.base_payload.copy()
    #         del payload[field]
    #
    #         response = self.client.post(path=self.url, data=payload)
    #
    #         self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
    #         self.assertIn(field, response.json())
    #
    # def test_device_register_invalid_device_type(self):
    #     """Test registration fails with invalid device type"""
    #     payload = self.base_payload.copy()
    #     payload['device_type'] = 'INVALID_TYPE'
    #
    #     response = self.client.post(path=self.url, data=payload)
    #
    #     self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
    #
    # def test_device_register_invalid_app_version(self):
    #     """Test registration fails with non-existent app version"""
    #     payload = self.base_payload.copy()
    #     payload['app_version'] = 99999
    #
    #     response = self.client.post(path=self.url, data=payload)
    #
    #     self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
    #
    # def test_device_register_inactive_app_version(self):
    #     """Test registration fails with inactive app version"""
    #     inactive_version = AppVersion.objects.create(
    #         version="0.9.0",
    #         force_update=False,
    #         device_type=DeviceType.ALL,
    #         is_active=False
    #     )
    #     payload = self.base_payload.copy()
    #     payload['app_version'] = inactive_version.id
    #
    #     response = self.client.post(path=self.url, data=payload)
    #
    #     self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
    #
    # def test_device_register_duplicate_device_id(self):
    #     """Test registering same device_id twice"""
    #     # First registration
    #     self.client.post(path=self.url, data=self.base_payload)
    #
    #     # Second registration with same device_id
    #     response = self.client.post(path=self.url, data=self.base_payload)
    #
    #     # Depending on your business logic, this might update or fail
    #     # Adjust assertion based on expected behavior
    #     self.assertIn(response.status_code, [status.HTTP_201_CREATED, status.HTTP_400_BAD_REQUEST])
    #
    # def test_device_register_invalid_ip_address(self):
    #     """Test registration with invalid IP address format"""
    #     payload = self.base_payload.copy()
    #     payload['ip_address'] = 'invalid-ip-address'
    #
    #     response = self.client.post(path=self.url, data=payload)
    #
    #     self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
    #
    # def test_device_register_invalid_language(self):
    #     """Test registration with invalid language code"""
    #     payload = self.base_payload.copy()
    #     payload['language'] = 'INVALID_LANG'
    #
    #     response = self.client.post(path=self.url, data=payload)
    #
    #     # Depending on validation, might succeed or fail
    #     self.assertIn(response.status_code, [status.HTTP_201_CREATED, status.HTTP_400_BAD_REQUEST])
    #
    # def test_device_register_invalid_theme(self):
    #     """Test registration with invalid theme"""
    #     payload = self.base_payload.copy()
    #     payload['theme'] = 'INVALID_THEME'
    #
    #     response = self.client.post(path=self.url, data=payload)
    #
    #     self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
    #
    # def test_device_register_empty_payload(self):
    #     """Test registration with empty payload"""
    #     response = self.client.post(path=self.url, data={})
    #
    #     self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
    #
    # def test_device_register_extra_fields_ignored(self):
    #     """Test that extra fields don't break registration"""
    #     payload = self.base_payload.copy()
    #     payload['extra_field'] = 'should_be_ignored'
    #
    #     response = self.client.post(path=self.url, data=payload)
    #
    #     self.assertEqual(status.HTTP_201_CREATED, response.status_code)
    #
    # def test_device_register_null_optional_fields(self):
    #     """Test registration with null optional fields"""
    #     payload = self.base_payload.copy()
    #     payload['firebase_token'] = None
    #
    #     response = self.client.post(path=self.url, data=payload)
    #
    #     # Adjust based on whether firebase_token is optional
    #     self.assertIn(response.status_code, [status.HTTP_201_CREATED, status.HTTP_400_BAD_REQUEST])
    #
    # def test_device_register_very_long_strings(self):
    #     """Test registration with very long string values"""
    #     payload = self.base_payload.copy()
    #     payload['device_model'] = 'A' * 1000
    #
    #     response = self.client.post(path=self.url, data=payload)
    #
    #     self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
    #
    # def test_device_register_special_characters(self):
    #     """Test registration with special characters in fields"""
    #     payload = self.base_payload.copy()
    #     payload['device_model'] = "iPhone <script>alert('xss')</script>"
    #
    #     response = self.client.post(path=self.url, data=payload)
    #
    #     # Should either sanitize or reject
    #     if response.status_code == status.HTTP_201_CREATED:
    #         device = Device.objects.get(device_id=payload['device_id'])
    #         self.assertNotIn('<script>', device.device_model)
    #
    # def test_device_register_response_structure(self):
    #     """Test that response has correct structure"""
    #     response = self.client.post(path=self.url, data=self.base_payload)
    #
    #     self.assertEqual(status.HTTP_201_CREATED, response.status_code)
    #     response_data = response.json()
    #
    #     self.assertIn('data', response_data)
    #     self.assertIn('device_token', response_data['data'])
    #     self.assertIsInstance(response_data['data']['device_token'], str)
    #
    # def test_device_register_device_token_format(self):
    #     """Test that device_token is a valid UUID format"""
    #     response = self.client.post(path=self.url, data=self.base_payload)
    #
    #     device_token = response.json().get('data', {}).get('device_token')
    #
    #     # Validate UUID format (assuming it's a UUID)
    #     import uuid
    #     try:
    #         uuid.UUID(device_token)
    #         token_is_valid = True
    #     except (ValueError, AttributeError):
    #         token_is_valid = False
    #
    #     self.assertTrue(token_is_valid)
    #
    # def test_device_register_database_persistence(self):
    #     """Test that device data is correctly saved to database"""
    #     response = self.client.post(path=self.url, data=self.base_payload)
    #
    #     device = Device.objects.get(device_id=self.base_payload['device_id'])
    #
    #     self.assertEqual(device.device_model, self.base_payload['device_model'])
    #     self.assertEqual(device.operation_version, self.base_payload['operation_version'])
    #     self.assertEqual(device.ip_address, self.base_payload['ip_address'])
    #
    # def test_device_register_case_sensitivity(self):
    #     """Test device_type case sensitivity"""
    #     payload = self.base_payload.copy()
    #     payload['device_type'] = 'ios'  # lowercase
    #
    #     response = self.client.post(path=self.url, data=payload)
    #
    #     # Depending on validation, might succeed if case-insensitive
    #     self.assertIn(response.status_code, [status.HTTP_201_CREATED, status.HTTP_400_BAD_REQUEST])
    #
    # def test_device_register_concurrent_requests(self):
    #     """Test handling of concurrent registration requests"""
    #     from concurrent.futures import ThreadPoolExecutor
    #
    #     def register_device(device_id):
    #         payload = self.base_payload.copy()
    #         payload['device_id'] = device_id
    #         return self.client.post(path=self.url, data=payload)
    #
    #     with ThreadPoolExecutor(max_workers=5) as executor:
    #         futures = [executor.submit(register_device, f'device-{i}') for i in range(5)]
    #         responses = [f.result() for f in futures]
    #
    #     success_count = sum(1 for r in responses if r.status_code == status.HTTP_201_CREATED)
    #     self.assertEqual(success_count, 5)
    #
    # def test_device_register_whitespace_handling(self):
    #     """Test that leading/trailing whitespace is handled properly"""
    #     payload = self.base_payload.copy()
    #     payload['device_model'] = '  iPhone 15 Pro  '
    #
    #     response = self.client.post(path=self.url, data=payload)
    #
    #     if response.status_code == status.HTTP_201_CREATED:
    #         device = Device.objects.get(device_id=payload['device_id'])
    #         # Should be trimmed or kept as-is based on serializer
    #         self.assertTrue(device.device_model.strip() == 'iPhone 15 Pro')
    #
    # def test_device_register_ipv6_address(self):
    #     """Test registration with IPv6 address"""
    #     payload = self.base_payload.copy()
    #     payload['ip_address'] = '2001:0db8:85a3:0000:0000:8a2e:0370:7334'
    #     payload['device_id'] = 'unique-device-ipv6'
    #
    #     response = self.client.post(path=self.url, data=payload)
    #
    #     self.assertEqual(status.HTTP_201_CREATED, response.status_code)
    #
    # def test_device_register_method_not_allowed(self):
    #     """Test that other HTTP methods are not allowed"""
    #     response = self.client.get(path=self.url)
    #     self.assertEqual(status.HTTP_405_METHOD_NOT_ALLOWED, response.status_code)
    #
    #     response = self.client.put(path=self.url, data=self.base_payload)
    #     self.assertEqual(status.HTTP_405_METHOD_NOT_ALLOWED, response.status_code)
    #
    #     response = self.client.delete(path=self.url)
    #     self.assertEqual(status.HTTP_405_METHOD_NOT_ALLOWED, response.status_code)
