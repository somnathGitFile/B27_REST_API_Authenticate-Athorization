from ast import Is
from django.shortcuts import render
from Custmor.serializer import CustomerSerializer
from .models import Customer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser,AllowAny
from rest_framework import viewsets
from Custmor.permissions import IsReadOnly, IsGetOrPostOrPut, RolePermission, OtherUserPermission, StaffUserPermission
# Create your views here.

class CustomerDetails(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    authentication_classes = [TokenAuthentication, ]
    #permission_classes = [IsReadOnly, ]
    #permission_classes = [IsGetOrPostOrPut, ]
    permission_classes = [StaffUserPermission, ]
    #permission_classes = [RolePermission, ]
    #permission_classes = [IsReadOnly, ]
