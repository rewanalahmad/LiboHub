from rest_framework import permissions


class IsOwnerOrReadonly(permissions.BasePermission):
    # Read permissions are allowed to any request,
    # so we'll always allow GET, HEAD or OPTIONS requests.
    
    def has_object_permations(self,request,view, object):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        #write the permations are only allowed to the owner of the request
        return object.owner== request.user 