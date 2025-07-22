from rest_framework import serializers
from .models import StudentProfile



class StudentProfileSerializer(serializers.ModelSerializer):
    user_id=serializers.IntegerField(source='user.id',read_only=True)
    user_name=serializers.CharField(source='user.full_name',read_only=True)
    class Meta:
        model= StudentProfile
        fields=['id','user_id','user_name','student_id','department','date_of_birth','address','phone_number','enrollment_year']
        read_only_fields=['id','user','student_id']