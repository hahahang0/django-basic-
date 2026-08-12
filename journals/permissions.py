from rest_framework.permissions import BasePermission


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in [
            'GET',"HEAD","OPTIONS"
        ]:
            return True
        return obj.author == request.user

class BlogpostPermission(BasePermission):
    def has_permission(self,request,view):
        if request.method in ["GET","HEAD","OPTIONS"]:
            return True 
        return request.user.is_authenticated;

    def has_object_permission(self, request, view, obj):
        if request.method in ["GET","HEAD","OPTIONS"]:
            return True 
        if request.method in ["PUT","PATCH"]:
            return obj.author == request.user 
        if request.method == "DELETE":
            return request.user.is_staff
        return False
        # return super().has_object_permission(request, view, obj)
