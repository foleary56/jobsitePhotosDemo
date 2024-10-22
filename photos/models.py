from django.db import models
from django.utils import timezone
import os

class Job(models.Model):
    name = models.CharField(max_length=255)
    # Add other fields as necessary

    def __str__(self):
        return self.name

def get_upload_path(instance, filename):
    job_name = instance.job.name.replace(" ", "_")
    photo_type = instance.photo_type
    date_uploaded = timezone.now().strftime("%Y-%m-%d")
    return os.path.join(f'{job_name}/{photo_type}/{date_uploaded}', filename)

class Photo(models.Model):
    PHOTO_TYPE_CHOICES = [
        ('before', 'Before'),
        ('during', 'During'),
        ('after', 'After'),
        ('issue', 'Issue'),
    ]
    
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='photos')
    photo_type = models.CharField(max_length=6, choices=PHOTO_TYPE_CHOICES)
    image = models.ImageField(upload_to=get_upload_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.photo_type.capitalize()} photo for {self.job.name}"
