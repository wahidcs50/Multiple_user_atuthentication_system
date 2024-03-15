from django.db import models
from django.conf import settings    
from django.db.models.signals import post_save
from django.dispatch import receiver
from registrations.models import Student, Alumni


class StudentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student_profile')
    field_of_study = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    date_of_birth = models.DateField(default='2000-01-01')
    address = models.TextField()
    degree = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    skills = models.TextField()

    def __str__(self):
        return self.user.email

class AlumniProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='alumni_profile')
    field_of_study = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    date_of_birth = models.DateField(default='2000-01-01')
    address = models.TextField()
    degree = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    graduation_year = models.IntegerField(default=2020)
    skills = models.TextField()

    def __str__(self):
        return self.user.email

@receiver(post_save, sender=Student)
def create_student_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'STUDENT':
        StudentProfile.objects.create(user=instance)

@receiver(post_save, sender=Alumni)
def create_alumni_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'ALUMNI':
        AlumniProfile.objects.create(user=instance)