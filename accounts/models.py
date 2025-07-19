from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
# Create your models here.


# Role constants
STUDENT='student'
TEACHER='teacher'
ADMIN='admin'
ADVISING_ADMIN='advising_admin'

ROLE_CHOICES=[
    (STUDENT,'Student'),
    (TEACHER,'Teacher'),
    (ADMIN,'Admin'),
    (ADVISING_ADMIN,'Advising Admin'),
]

class CustomUserManager(BaseUserManager):
    def create_user(self,email,full_name,role,password=None,**extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email=self.normalize_email(email)
        user=self.model(email=email,full_name=full_name,role=role,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,full_name,role="admin",password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        return self.create_user(email,full_name,role,password,**extra_fields)
    

class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(unique=True)
    full_name=models.CharField(max_length=100)
    role=models.CharField(max_length=20,choices=ROLE_CHOICES)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    date_joined=models.DateTimeField(auto_now_add=True)
    objects=CustomUserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['full_name','role']

    def __str__(self):
        return f"{self.full_name} ({self.role})"