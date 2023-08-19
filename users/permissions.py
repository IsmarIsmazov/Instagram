from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == SAFE_METHODS:
            return True

        return request.user == obj.username


class IsOwnerPermissionClass(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == SAFE_METHODS:
            return True

        return request.user == obj.author