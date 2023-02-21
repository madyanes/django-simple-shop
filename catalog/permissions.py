from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    The request is authenticated as a staff user, or is a read-only request.
    """
    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user.is_staff
        )


class IsOwner(permissions.BasePermission):
    """
    The request is only for the owner of that object/instance.
    """
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
