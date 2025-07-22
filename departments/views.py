from django.shortcuts import render

# Create your views here.
from rest_framework import generics,permissions
from . models import Department
from .serializers import DepartmentSerializer

class DepartmentListView(generics.ListAPIView):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer
    permission_classes=[permissions.IsAuthenticated]

class DepartmentListCreateApiView(generics.ListCreateAPIView):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer
    permission_classes=[permissions.IsAdminUser]

class DepartmentDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer
    permission_classes=[permissions.IsAdminUser]