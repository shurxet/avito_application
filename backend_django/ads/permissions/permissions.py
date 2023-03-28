from rest_framework import permissions
from users.models import User


class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user.role == User.Role.ADMIN


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user and request.user and obj.author == request.user


class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.role == User.is_superuser:
            return True

        if view.action == 'retrieve':
            return True

        if view.action in ["create", "update", "partial_update", "destroy"]:
            return obj.author == request.user or request.user.role == User.Role.ADMIN
