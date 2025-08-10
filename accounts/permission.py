from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrAdvisingAdminOrReadOnly(BasePermission):
    def has_permission(self,request,view):
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated
        
        return(
            request.user.is_authenticated and
            request.user.role in ['admin','advising_admin']
        )
            # improve version of has_permission method
# def has_permission(self, request, view):
#     if not request.user.is_authenticated:
#         return False
        
#     if request.method in SAFE_METHODS:
#         return True
        
#     # Ensure user has a valid role
#     if not hasattr(request.user, 'role'):
#         return False
        
#     return request.user.role in ['admin', 'advising_admin']
    
# we can use it later
class IsStudentSelfOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.role in ['admin', 'advising_admin']:
            return True
        return request.user == obj and request.user.role == 'student'
    
class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and 
            request.user.role == "admin"  # Only 'admin' role is super admin
        )

class IsAccountCreatorAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and 
            request.user.role == "account_creator_admin"
        )
    
class IsSuperAdminOrAccountCreatorAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role in ['admin', 'account_creator_admin']
        )

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and 
            request.user.role == "student"
        )

class IsAdminOrAdvisingAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role in ["admin", "advising_admin"]
        )