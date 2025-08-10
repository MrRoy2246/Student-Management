from django.db import models
from django.conf import settings
from departments.models import Department
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import datetime
# Create your models here.


class StudentProfile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    student_id=models.CharField(max_length=20,unique=True)
    department=models.ForeignKey(Department,on_delete=models.SET_NULL,null=True,blank=True,related_name='students')  # Add this related_name
    date_of_birth=models.DateField(null=True,blank=True)
    address=models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)#will validate later
    enrollment_year = models.PositiveIntegerField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='student_pics/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def clean(self):
    #     if self.enrollment_year and self.enrollment_year > datetime.date.today().year:
    #         raise ValidationError("Enrollment year cannot be in the future")


    def __str__(self):
        return f"{self.user.full_name} - {self.student_id}"
    




        """phone_number = models.CharField(
        max_length=20, 
        blank=True,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]
    )
        """