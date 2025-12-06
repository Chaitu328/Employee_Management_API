from rest_framework.permissions import BasePermission

class IsHRForDelete(BasePermission):
    def has_permission(self, request, view):
        if request.method == "DELETE":
            department = request.query_params.get("department")
            return department == "HR"
        return True