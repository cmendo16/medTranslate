from rest_framework import permissions 

# Check if user owns phrase, or if the phrase is default 
class IsOwnerOrDefaultReadOnly(permissions.BasePermission): 
    """
    Default phrase (is_default =True): read-only for everyone. 
    User Phrases: only the owner can modify/delete. 
    
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are always allowed 
        if request.method in permissions.SAFE_METHODS:
            return True
        
        #Writes on default phrases are denied
        if obj.is_default: 
            return False; 
        
        #otherwise, users are allowed to write their own phrases 
        return obj.added_by_id == getattr(request.user, "id", None)