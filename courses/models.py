# from django.db import models

# # Create your models here.
# from student_course_mgmt import settings


# class Course(models.Model):
#     name = models.CharField(max_length=100)
#     course_code = models.CharField(max_length=50, unique=True)  # e.g. CSE101
#     department = models.CharField(max_length=100)
#     credits = models.PositiveIntegerField(default=3)

#     def __str__(self):
#         return f"{self.course_code} - {self.name}"

# class Section(models.Model):
#     course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='sections')
#     teacher=models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.PROTECT,
#         null=False,
#         limit_choices_to={'role':'teacher'},
#         related_name='sections'
#     )
#     section=models.CharField(max_length=50)
#     schedule=models.CharField(max_length=50)
#     room=models.CharField(max_length=50,null=True,blank=True)
#     seats=models.PositiveBigIntegerField(default=30)

#     def __str__(self):
#         return f"{self.course.course_code} - Section {self.section}"