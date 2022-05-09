from django.shortcuts import render
from EmpAuth.serializer import EmployeeSerializer
from .models import Employee
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser,AllowAny
from rest_framework import viewsets
from EmpAuth.permissions import IsReadOnly, IsGetOrPostOrPut, RolePermission, OtherUserPermission
# Create your views here.

class EmployeeDetails(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]