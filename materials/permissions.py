from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    message = "You are not moderator"

    def has_permission(self, request, view):
        return request.user.groups.filter(name='moderator').exists()


class IsOwner(BasePermission):
    message = "You are not owner"

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user