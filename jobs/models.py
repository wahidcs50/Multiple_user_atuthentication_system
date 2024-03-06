from django.db import models
from django.contrib.auth import get_user_model
class Job(models.Model):
    CAREER_TYPES = [
        ('Job', 'Job'),
        ('Internship', 'Internship'),
    ]

    APPLICATION_STATUSES = [
        ('Pending', 'Pending'),
        ('Applied', 'Applied'),
        ('Expired', 'Expired'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField()
    date_posted = models.DateField()
    employer_organization = models.CharField(max_length=255)
    duration_in_months = models.IntegerField(default=0)
    career_type = models.CharField(max_length=10, choices=CAREER_TYPES)
    
    # # New field for application status
    # application_status = models.CharField(max_length=10, choices=APPLICATION_STATUSES, default='Pending')

    def __str__(self):
        return self.title

class StudentCareerApplication(models.Model):
    APPLICATION_STATUSES = [
        ('Pending', 'Pending'),
        ('Applied', 'Applied'),
        ('Expired', 'Expired'),
    ]

    student = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    career = models.ForeignKey(Job, on_delete=models.CASCADE)
    application_status = models.CharField(max_length=10, choices=APPLICATION_STATUSES, default='Pending')

    def __str__(self):
        return f"{self.student.username} - {self.career.title} - {self.application_status}"

