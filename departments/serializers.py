from . models import Department
from rest_framework import serializers
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields=['id','name','code']
    
    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty")
        return value.strip()

    def validate_code(self, value):
        if not value.strip():
            raise serializers.ValidationError("Code cannot be empty")
        return value.strip()
