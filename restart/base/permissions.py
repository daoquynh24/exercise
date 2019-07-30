from rest_framework.permissions import BasePermission
from .constants.common import AppConstants


class IsAdmin(BasePermission):
    message = 'Require ADMIN role'

    def has_permission(self, request, view):
        return request.user.id and request.user.role_id == AppConstants.Role.Admin


class IsUser(BasePermission):
    message = 'Require USER role'

    def has_permission(self, request, view):
        return request.user.id and request.user.role_id == AppConstants.Role.User
