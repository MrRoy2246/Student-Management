from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrAdvisingAdminOrReadOnly(BasePermission):
    def has_permission(self,request,view):
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated
        
        return(
            request.user.is_authenticated and
            request.user.role in ['admin','advising_admin']
        )
    
# we can use it later
class IsStudentSelfOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.role in ['admin', 'advising_admin']:
            return True
        return request.user == obj and request.user.role == 'student'