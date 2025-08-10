# from django.shortcuts import render

# # Create your views here.
# from rest_framework import generics,permissions
# from . models import Department
# from .serializers import DepartmentSerializer
# from accounts.permission import IsSuperAdmin

# class DepartmentListView(generics.ListAPIView):
#     queryset=Department.objects.all()
#     serializer_class=DepartmentSerializer
#     permission_classes=[permissions.IsAuthenticated]

# class DepartmentListCreateApiView(generics.ListCreateAPIView):
#     queryset=Department.objects.all()
#     serializer_class=DepartmentSerializer
#     permission_classes=[IsSuperAdmin]

# class DepartmentDetailApiView(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Department.objects.all()
#     serializer_class=DepartmentSerializer
#     permission_classes=[permissions.IsAdminUser]

from rest_framework import generics, permissions
from .models import Department
from .serializers import DepartmentSerializer
from accounts.permission import IsSuperAdmin

class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.filter(is_active=True)
    serializer_class = DepartmentSerializer
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAuthenticated()]
        return [IsSuperAdmin()]

class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.filter(is_active=True)
    serializer_class = DepartmentSerializer
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAuthenticated()]
        return [IsSuperAdmin()]
    
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()