from rest_framework.permissions import BasePermission,SAFE_METHODS



class IsAdminP(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff



    def has_permission(self, request, view):
        if request.user.role in ['manager','seller']:
            return True
        else:
            return False

class IsOwners(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        if request.user.is_staff:
            return True
        
        return request.user == obj.user
