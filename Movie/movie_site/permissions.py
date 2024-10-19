from rest_framework import permissions

class CheckOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.status_profile == 'pro':
            return True

        if request.user.status_profile == 'simple' and obj.status_movie == 'simple':
            return True

        return False