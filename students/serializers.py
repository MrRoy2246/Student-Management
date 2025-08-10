from rest_framework import serializers
from .models import StudentProfile
from departments .models import Department


class StudentProfileSerializer(serializers.ModelSerializer):
    user_id=serializers.IntegerField(source='user.id',read_only=True)
    user_name=serializers.CharField(source='user.full_name',read_only=True)
    department_name = serializers.CharField(source='department.name', read_only=True)
    department_code = serializers.CharField(source='department.code', read_only=True)
    # department = serializers.SlugRelatedField(
    #     slug_field='name',
    #     queryset=Department.objects.filter(is_active=True),
    #     allow_null=True
    # )
    class Meta:
        model= StudentProfile
        fields=['id','user_id','user_name','student_id','department_name','department_code','date_of_birth','address','phone_number','enrollment_year']
        read_only_fields=['id','user','student_id']
    def update(self, instance, validated_data):
        validated_data.pop('user', None)  # prevent user update
        return super().update(instance, validated_data)

class AdminStudentProfileSerializer(serializers.ModelSerializer):
    user_id=serializers.IntegerField(source='user.id',read_only=True)
    user_name=serializers.CharField(source='user.full_name')
    # department = serializers.SlugRelatedField(
    #     slug_field='name',
    #     queryset=Department.objects.filter(is_active=True),
    #     allow_null=True
    # )
    class Meta:
        model= StudentProfile
        fields=['id','user_id','user_name','student_id','department','date_of_birth','address','phone_number','enrollment_year']
        read_only_fields=['id','user','student_id']
    def update(self,instance,validated_data):
        user_data=validated_data.pop('user',{})
        if user_data:
            instance.user.full_name=user_data.get("full_name",instance.user.full_name)
            instance.user.save()
        return super().update(instance,validated_data)