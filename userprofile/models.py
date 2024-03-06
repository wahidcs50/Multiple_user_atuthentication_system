from django.db import models
from django.conf import settings


# Create your models here.
class StudentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student_profile')
    # Add fields specific to student profile
    # student = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, null=True, blank= True)
    field_of_study = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    address = models.TextField()
    degree = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    skills = models.TextField()
    def __str__(self):
        return self.user.email
    

class AlumniProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='alumni_profile')
    # Add fields specific to alumni profile
    field_of_study = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    address = models.TextField()
    degree = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    graduation_year = models.IntegerField()
    skills = models.TextField()
    def __str__(self):
        return self.user.email
    