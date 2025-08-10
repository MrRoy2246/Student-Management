from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer,LoginSerializer,ProfileSerializer
from django.contrib.auth import authenticate,get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from departments.models import Department
from students .models import StudentProfile
from . models import User
from students.signals import generate_student_id
from .permission import IsAccountCreatorAdmin
from .serializers import AdminCreationSerializer
from .permission import IsSuperAdmin,IsSuperAdminOrAccountCreatorAdmin 
class RegisterView(APIView):
    permission_classes = [IsSuperAdminOrAccountCreatorAdmin]  
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            # Extract department_name from validated data
            department_name = serializer.validated_data.get('department_name', None)
            
            # Create the user
            user = serializer.save()
            
            # If user is a student, create profile with department
            if user.role == 'student':
                if department_name:
                    try:
                        department = Department.objects.get(name=department_name, is_active=True)
                    except Department.DoesNotExist:
                        # If department doesn't exist, use default
                        department, _ = Department.objects.get_or_create(
                            name="Undeclared",
                            defaults={'code': 'UNDEC'}
                        )
                else:
                    # No department specified, use default
                    department, _ = Department.objects.get_or_create(
                        name="Undeclared",
                        defaults={'code': 'UNDEC'}
                    )
                
                StudentProfile.objects.create(
                    user=user,
                    student_id=generate_student_id(),
                    department=department
                )
            
            return Response({
                "message": "User created successfully",
                "user": {
                    "email": user.email,
                    "full_name": user.full_name,
                    "role": user.role
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            # user = authenticate(request, email=email, password=password)
            try:
                user=User.objects.get(email=email)
            except User.DoesNotExist:
                return Response(
                    {"status": "error", "message": "Invalid credentials"},
                    status=status.HTTP_401_UNAUTHORIZED
                )
            if not user.check_password(password):
                return Response(
                    {"status": "error", "message": "Invalid credentials"},
                    status=status.HTTP_401_UNAUTHORIZED
                )
            if not user.is_active:
                return Response(
                    {"status": "error", "message": "Account is disabled"},
                    status=status.HTTP_403_FORBIDDEN
                )
            refresh = RefreshToken.for_user(user)
            return Response({
                "status": "success",
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "user": {
                    "email": user.email,
                    "full_name": user.full_name,
                    "role": user.role
                }
            }, status=status.HTTP_200_OK)
        return Response(
        {"status": "error", "message": serializer.errors},
        status=status.HTTP_400_BAD_REQUEST
        )

class ProfileView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        serializer=ProfileSerializer(request.user)
        return Response({"status":"Success","data":serializer.data},status=status.HTTP_200_OK)
    def put(self,request):
        serializer=ProfileSerializer(request.user,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Status":"Success","data":serializer.data},status=status.HTTP_200_OK)
        return Response({"Status":"Error","message":serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)


# test
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class ProtectedTestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": f"Hello, {request.user.full_name}! You are authenticated."})
    



class AdminCreationView(APIView):
    permission_classes = [IsSuperAdmin]  # Only existing admins can create other admins
    
    def post(self, request):
        serializer = AdminCreationSerializer(data=request.data)
        if serializer.is_valid():
            admin = serializer.save()
            return Response({
                "message": "Admin created successfully",
                "admin": {
                    "email": admin.email,
                    "full_name": admin.full_name,
                    "role": admin.role
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
