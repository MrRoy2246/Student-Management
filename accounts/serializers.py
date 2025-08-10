from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password
from departments.models import Department


class RegisterSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(write_only=True,required=True,label="Confirm Password")
    role = serializers.CharField(required=True)
    department_name=serializers.CharField(required=True,write_only=True)

    class Meta:
        model=User
        fields=('email','full_name','role','password','password2',"department_name")
        extra_kwargs={
            'password':{'write_only':True}
        }

    def validate(self,attrs):
        if attrs['password']!=attrs['password2']:
            raise serializers.ValidationError({"password":"Password field did not match"})
        # for test we commend this this is django's build in password validation
        # validate_password(attrs['password'])
        return attrs
    def validate_role(self,value):
        allowed_roles = ["student", "teacher"]
        if value not in allowed_roles:
            raise serializers.ValidationError(f"Cannot create user with role '{value}'. Allowed roles: student, teacher")
        return value
    def validate_department_name(self, value):
        # Only validate if role is student and department_code is provided
        if self.initial_data.get('role') == 'student' and value:
            try:
                Department.objects.get(name=value, is_active=True)
            except Department.DoesNotExist:
                raise serializers.ValidationError("Invalid department code")
        return value
    def create(self,validated_data):
        validated_data.pop('password2')
        # department_name = validated_data.pop('department_name', None)
        user=User.objects.create_user(
            email=validated_data['email'],
            full_name=validated_data['full_name'],
            role=validated_data['role'],
            password=validated_data['password']
        )
        return user
class LoginSerializer(serializers.Serializer):
    email= serializers.EmailField(required=True)
    password=serializers.CharField(write_only=True,required=True)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email','full_name','role']
        read_only_fields=('email','role')


class AdminCreationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True, label="Confirm Password")
    
    class Meta:
        model = User
        fields = ('email', 'full_name', 'role', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields did not match"})
        
        # Uncomment for production
        # validate_password(attrs['password'])
        return attrs
    
    def validate_role(self, value):
        # Only allow admin roles to be created
        allowed_roles = ["advising_admin", "account_creator_admin"]
        if value not in allowed_roles:
            raise serializers.ValidationError(f"Cannot create admin with role '{value}'. Allowed roles: advising_admin, account_creator_admin")
        return value
    
    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(
            email=validated_data['email'],
            full_name=validated_data['full_name'],
            role=validated_data['role'],
            password=validated_data['password']
        )
        return user