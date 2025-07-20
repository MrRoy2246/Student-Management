from .models import Course,Section
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=['id','name','course_code','department','credits']
    
class SectionSerializer(serializers.ModelSerializer):
    course_name=serializers.CharField(source='course.name',read_only=True)
    teacher_name=serializers.CharField(source='teacher.full_name',read_only=True)
    class Meta:
        model=Section
        fields=['id','course','course_name','teacher','teacher_name','section','schedule','room','seats']
    def validate_teacher(self, value):
        if value.role != 'teacher':
            raise serializers.ValidationError("Selected user is not a teacher.")
        return value