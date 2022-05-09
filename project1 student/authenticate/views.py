from django.shortcuts import render
from authenticate.models import Student
from rest_framework import viewsets
from authenticate.serializer import StudentSerializer
from authenticate.serializer import StudentSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

# Create your views here.
class StudentDetails(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = [AllowAny, ]