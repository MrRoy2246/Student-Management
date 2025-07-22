from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import StudentProfile
from accounts.models import User
def generate_student_id():
    last_student = StudentProfile.objects.order_by('-id').first()
    if last_student and last_student.student_id:
        try:
            last_id = int(last_student.student_id.split('-')[-1])
            return f"STU-{str(last_id + 1).zfill(3)}"
        except (ValueError, IndexError):
            # fallback if student_id is malformed
            pass
    return "STU-001"

@receiver(post_save,sender=User)
def create_student_profile(sender,instance,created,**kwargs):
    if created and instance.role =='student':
        StudentProfile.objects.create(user=instance,
                                      student_id=generate_student_id())