from rest_framework import permissions

class IsOwnerOrEditorReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    Editors can view all entries but cannot edit them unless they own them.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed if the user is in the "Editor" group or is the owner
        is_editor = request.user.groups.filter(name='Editor').exists()
        
        if request.method in permissions.SAFE_METHODS:
            return obj.author == request.user or is_editor
            
        # Write permissions are only allowed to the author of the entry
        return obj.author == request.user
