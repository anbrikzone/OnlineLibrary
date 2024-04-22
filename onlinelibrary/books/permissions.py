from rest_framework import permissions
from rest_framework.permissions import BasePermission


class isOwner(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        request.user
        return obj.user == request.user