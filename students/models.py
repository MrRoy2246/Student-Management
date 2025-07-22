from django.db import models
from django.conf import settings
from departments.models import Department
# Create your models here.


class StudentProfile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    student_id=models.CharField(max_length=20,unique=True)
    department=models.ForeignKey(Department,on_delete=models.SET_NULL,null=True,blank=True)
    date_of_birth=models.DateField(null=True,blank=True)
    address=models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    enrollment_year = models.PositiveIntegerField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='student_pics/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.user.full_name} - {self.student_id}"