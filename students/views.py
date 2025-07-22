from django.shortcuts import render
from rest_framework import generics,permissions
from . models import StudentProfile
from .serializers import StudentProfileSerializer
from rest_framework.exceptions import NotFound
# Create your views here.



class StudentOwnProfileView(generics.RetrieveUpdateAPIView):
    serializer_class=StudentProfileSerializer
    permission_classes=[permissions.IsAuthenticated]
    def get_object(self):
        try:
            return StudentProfile.objects.get(user=self.request.user, is_active=True)
        except StudentProfile.DoesNotExist:
            raise NotFound("Student profile not found")
class StudentProfileListView(generics.ListAPIView):
    serializer_class=StudentProfileSerializer
    permission_classes=[permissions.IsAdminUser]
    queryset=StudentProfile.objects.all()
