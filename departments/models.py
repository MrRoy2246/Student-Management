from django.db import models
from django.core.validators import RegexValidator
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(
        max_length=50,
        unique=True,
        validators=[RegexValidator(r'^[A-Z0-9-]+$', 'Code must be uppercase letters, numbers, or hyphens')]
    )
    # if we want to add soft delete in future thats why is_active
    # also then in vew  we use this for clean api response ---------->queryset = Department.objects.filter(is_active=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def get_student_count(self):
        # Import here to avoid circular import
        from students.models import StudentProfile
        return StudentProfile.objects.filter(department=self, is_active=True).count()

    def __str__(self):
        return f"{self.code} - {self.name}"