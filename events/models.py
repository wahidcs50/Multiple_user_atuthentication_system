from django.db import models
from django.contrib.auth import get_user_model

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.title
class Notification(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    link = models.CharField(max_length=255)  # Store URLs here
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
