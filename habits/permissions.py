from rest_framework.permissions import BasePermission


class IsSuperUser(BasePermission):
    message = 'You are not a superuser!'

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False


class IsOwner(BasePermission):
    message = 'You are not the owner!'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return False
