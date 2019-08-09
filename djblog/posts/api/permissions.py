from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadonly(BasePermission):
    message = "You haven't permission on review other user"
    safe_methods = ['GET', 'OPTION', 'HEAD']

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

    def has_object_permission(self, request, view, obj):
        if request.method in self.safe_methods:
            return True
        return obj.user == request.user
