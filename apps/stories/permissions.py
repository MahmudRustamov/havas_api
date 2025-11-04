from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    GET, HEAD, OPTIONS hamma uchun.
    POST, PUT, DELETE faqat superuser uchun.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff
