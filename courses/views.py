from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from .models import Course,Section
from .serializers import CourseSerializer,SectionSerializer
from accounts.permission import IsAdminOrAdvisingAdminOrReadOnly

class CourseViewSet(ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer
    permission_classes=[IsAdminOrAdvisingAdminOrReadOnly]

class SectionViewset(ModelViewSet):
    queryset=Section.objects.all()
    serializer_class=SectionSerializer
    permission_classes=[IsAdminOrAdvisingAdminOrReadOnly]