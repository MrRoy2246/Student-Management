from . models import Department
from rest_framework import serializers
class DepartmentSerializer(serializers.ModelSerializer):
    student_count = serializers.SerializerMethodField()
    class Meta:
        model=Department
        fields=['id','name','code','student_count']

    def get_student_count(self, obj):
        return obj.students.filter(is_active=True).count()
    
    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty")
        return value.strip()

    def validate_code(self, value):
        if not value.strip():
            raise serializers.ValidationError("Code cannot be empty")
        return value.strip()
