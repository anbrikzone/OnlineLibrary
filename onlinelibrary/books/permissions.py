from rest_framework.permissions import BasePermission

class isOwnerOrSuperUser(BasePermission):
    
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        print(obj.user)
        if request.user.is_superuser or obj.user == request.user:
           return True
        return False