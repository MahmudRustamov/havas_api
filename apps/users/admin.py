from django.contrib.auth.admin import UserAdmin

from apps.users.models.user import User
from django.contrib import admin
from apps.users.models.device import Device, AppVersion


@admin.register(AppVersion)
class AppVersionAdmin(admin.ModelAdmin):
    list_display = ('version', 'device_type', 'is_active', 'force_update', 'created_at')
    list_filter = ('device_type', 'is_active', 'force_update')
    search_fields = ('version',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('App Version Info', {
            'fields': ('version', 'description', 'device_type')
        }),
        ('Status', {
            'fields': ('is_active', 'force_update')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
        }),
    )


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'device_type', 'device_model',
        'ip_address', 'language', 'theme', 'is_active', 'last_login'
    )
    list_filter = (
        'device_type', 'language', 'theme', 'is_active', 'is_push_notification'
    )
    search_fields = (
        'device_model', 'device_id', 'user__username', 'user__email', 'ip_address'
    )
    readonly_fields = ('device_token', 'first_login', 'last_login', 'logged_out_at')
    ordering = ('-last_login',)
    autocomplete_fields = ('user', 'app_version')

    fieldsets = (
        ('Device Info', {
            'fields': (
                'user', 'device_type', 'device_model', 'operation_version',
                'device_id', 'ip_address', 'app_version'
            )
        }),
        ('Preferences', {
            'fields': ('language', 'theme', 'is_push_notification', 'is_auth_password')
        }),
        ('Status', {
            'fields': ('is_active', 'logged_out_at', 'device_token')
        }),
        ('Timestamps', {
            'fields': ('first_login', 'last_login'),
        }),
    )

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'phone_number', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'phone_number')
    ordering = ('-created_at',)