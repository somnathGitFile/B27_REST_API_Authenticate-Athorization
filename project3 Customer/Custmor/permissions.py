from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            print(dir(SAFE_METHODS))
            return True
        else:
            return False

class IsGetOrPostOrPut(BasePermission):
    def has_permission(self, request, view):
        allowed_method = ['GET', 'POST', 'PUT']
        if request.method in allowed_method:
            return True
        else:
            return False

class RolePermission(BasePermission):
    def has_permission(self, request, view):
        status = request.user.is_superuser #only superuser or admim can do CRUD
        if status == True:
            allowed_method = ['GET', 'POST', 'PUT', 'DELETE']
            if request.method in allowed_method:
                return True
            else:
                return False

        else:
            if request.method in SAFE_METHODS:
                return True
            else:
                return False

class OtherUserPermission(BasePermission):
    def has_permission(self, request, view):
        status = request.user.is_authenticated #authenticated users can do CRUD
        print(dir(request.user))
        if status == True:
            allowed_method =['GET', 'POST','PUT','DELETE']
            if request.method in allowed_method:
                return True
            else:
                return False


class StaffUserPermission(BasePermission):
    def has_permission(self, request, view):
        status = request.user.is_staff #staff users can do CRUD
        if status == True:
            allowed_method =['GET', 'POST','PUT','DELETE']
            if request.method in allowed_method:
                return True
            else:
                return False
