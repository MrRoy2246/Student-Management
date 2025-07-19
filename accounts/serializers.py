from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(write_only=True,required=True,label="Confirm Password")

    class Meta:
        model=User
        fields=('email','full_name','role','password','password2')
        extra_kwargs={
            'password':{'write_only':True}
        }

    def validate(self,attrs):
        if attrs['password']!=attrs['password2']:
            raise serializers.ValidationError({"password":"Password field did not match"})
        return attrs
    def create(self,validated_data):
        validated_data.pop('password2')
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