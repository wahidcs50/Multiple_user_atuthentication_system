# profiles/models.py
from django.db import models
from django.contrib.auth import get_user_model

class StudentProfile(models.Model):
    student = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, null=True, blank= True)
    field_of_study = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    # profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    # Add other core fields

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name}'s Profile"

class PersonalInfo(models.Model):
    student = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    date_of_birth = models.DateField()
    address = models.TextField()
    # Add other personal info fields

class Education(models.Model):
    student = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, null=True, )
    degree = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    graduation_year = models.IntegerField()
    # Add other education fields

class Skills(models.Model):
    student = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, null=True,  blank=True )
    skills = models.TextField()

# class Resume(models.Model):
#     profile = models.OneToOneField(StudentProfile, on_delete=models.CASCADE)
#     resume_file = models.FileField(upload_to='resumes/')
