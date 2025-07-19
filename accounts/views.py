from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer,LoginSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
class RegisterView(APIView):
    def post(self,request):
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            return Response({
                "message":"User Register Successfully",
                "user":{
                    "email":user.email,
                    "full_name":user.full_name,
                    "role":user.role
                }
            },status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    def post(self,request):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            email=serializer.validated_data['email']
            password=serializer._validated_data['password']

            user=authenticate(request,email=email,password=password)
            if user is not None:
                refresh=RefreshToken.for_user(user)
                return Response({
                    "access":str(refresh.access_token),
                    "refresh":str(refresh),
                    "user":{
                        "email":user.email,
                        "full_name":user.full_name,
                        "role":user.role
                    }
                }, status=status.HTTP_200_OK)
            else:
                return Response({"detail":"Invalid Credientials"},status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            


# test
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class ProtectedTestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": f"Hello, {request.user.full_name}! You are authenticated."})
