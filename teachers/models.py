from django.db import models
from django.conf import settings
from departments.models import Department
# Create your models here.


class TeacherProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    teacher_id = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)

    designation = models.CharField(max_length=100)  # e.g. Lecturer, Professor
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)

    joining_date = models.DateField(null=True, blank=True)
    qualifications = models.TextField(blank=True)  # Or JSONField if structured data is needed
    experience_years = models.PositiveIntegerField(null=True, blank=True)
    office_room_number = models.CharField(max_length=20, blank=True)
    available_for_advising = models.BooleanField(default=False)
    schedule_url = models.URLField(blank=True, null=True)

    profile_picture = models.ImageField(upload_to='teacher_pics/', null=True, blank=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.full_name} - {self.teacher_id}"
