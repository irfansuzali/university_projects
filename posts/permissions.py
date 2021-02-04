from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        #If the request method is one of the HTTTP SAFE_METHODS (GET, OPTIONS, HEAD), read only permission granted
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user