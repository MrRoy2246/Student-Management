from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import TeacherProfile
from accounts.models import User
def generate_teacher_id():
    last_teacher = TeacherProfile.objects.order_by('-id').first()
    if last_teacher and last_teacher.teacher_id:
        try:
            last_id = int(last_teacher.teacher_id.split('-')[-1])
            return f"TEA-{str(last_id + 1).zfill(3)}"
        except (ValueError, IndexError):
            # fallback if student_id is malformed
            pass
    return "TEA-001"

@receiver(post_save,sender=User)
def create_teacher_profile(sender,instance,created,**kwargs):
    if created and instance.role =='teacher':
        TeacherProfile.objects.create(user=instance,
                                      teacher_id=generate_teacher_id())