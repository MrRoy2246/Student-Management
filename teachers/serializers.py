from rest_framework import serializers
from .models import TeacherProfile


class TeacherProfileSerializer(serializers.ModelSerializer):
    user_id=serializers.IntegerField(source='user.id',read_only=True)
    user_name=serializers.CharField(source='user.full_name',read_only=True)
    # department = serializers.SlugRelatedField(
    #     slug_field='name',
    #     queryset=Department.objects.filter(is_active=True),
    #     allow_null=True
    # )
    class Meta:
        model= TeacherProfile
        fields=['id','user_id','user_name','teacher_id','designation','department','date_of_birth','address','phone_number','qualifications','experience_years','office_room_number']
        read_only_fields=['id','user_id','student_id']
    def update(self, instance, validated_data):
        validated_data.pop('user', None)  # prevent user update
        return super().update(instance, validated_data)

class AdminTeacherProfileSerializer(serializers.ModelSerializer):
    user_id=serializers.IntegerField(source='user.id',read_only=True)
    user_name=serializers.CharField(source='user.full_name')
    # department = serializers.SlugRelatedField(
    #     slug_field='name',
    #     queryset=Department.objects.filter(is_active=True),
    #     allow_null=True
    # )
    class Meta:
        model= TeacherProfile
        fields=['id','user_id','user_name','teacher_id','designation','department','date_of_birth','address','phone_number','qualifications','experience_years','office_room_number']
        read_only_fields=['id','user_id','student_id']
    def update(self,instance,validated_data):
        user_data=validated_data.pop('user',{})
        if user_data:
            instance.user.full_name=user_data.get("full_name",instance.user.full_name)
            instance.user.save()
        return super().update(instance,validated_data)