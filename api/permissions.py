from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
    # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
            # Write permissions are only allowed to the author of a post
        return obj.owner == request.user

class IsAuthorOrReadOnly1(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
    # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
            # Write permissions are only allowed to the author of a post
        return obj.phone.owner == request.user

class IsAuthorOrReadOnly2(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
    # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
            # Write permissions are only allowed to the author of a post
        return obj.user.username == request.user

class IsUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
    # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
            # Write permissions are only allowed to the author of a post
        return obj == request.user