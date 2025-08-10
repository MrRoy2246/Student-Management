from django.shortcuts import render
from rest_framework import generics,permissions
from . models import StudentProfile
from rest_framework.response import Response
from .serializers import StudentProfileSerializer,AdminStudentProfileSerializer
from rest_framework.exceptions import NotFound
from accounts.permission import IsStudent,IsAdminOrAdvisingAdmin
# Create your views here.



class StudentOwnProfileView(generics.RetrieveUpdateAPIView):
    serializer_class=StudentProfileSerializer
    permission_classes=[IsStudent]
    def get_object(self):
        try:
            return StudentProfile.objects.get(user=self.request.user, is_active=True)
        except StudentProfile.DoesNotExist:
            raise NotFound("Student profile not found")
class StudentProfileListView(generics.ListAPIView):
    serializer_class=StudentProfileSerializer
    permission_classes=[IsAdminOrAdvisingAdmin]
    queryset=StudentProfile.objects.all()
class StudentProfileDetailView(generics.RetrieveUpdateAPIView):
    queryset=StudentProfile.objects.filter(is_active=True)
    serializer_class=AdminStudentProfileSerializer
    permission_classes=[IsAdminOrAdvisingAdmin]

    # def retrieve(self, request, *args, **kwargs):
    #     response=super().retrieve(request, *args, **kwargs)
    #     return Response({"Status":"Success","data":response.data},status=response.status_code)
    # def update(self, request, *args, **kwargs):
    #     response= super().update(request, *args, **kwargs)
    #     return Response({"Status":"Success","data":response.data},status=response.status_code)