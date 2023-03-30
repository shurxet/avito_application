from rest_framework import permissions
from users.models import User


class AdPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if view.action == 'list':
            return request.user.is_anonymous

        if view.action == 'retrieve':
            return request.user.is_authenticated

        if view.action in ["create", "update", "partial_update", "destroy"]:
            return obj.author == request.user or request.user.role == User.Role.ADMIN
