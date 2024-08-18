from django.db import models
from django.utils import timezone


class Luggage(models.Model):
    id = models.BigAutoField(primary_key=True)  # Explicit primary key
    storage_time = models.DateTimeField(default=timezone.now)
    luggage_name = models.CharField(max_length=255)
    luggage_size = models.CharField(max_length=255)
    luggage_description = models.TextField(blank=True, null=True)
    images = models.ManyToManyField('Image', blank=True)

    def __str__(self):
        return self.luggage_name


class Image(models.Model):
    id = models.BigAutoField(primary_key=True)  # Explicit primary key
    image = models.ImageField(upload_to='luggage_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id} - {self.uploaded_at}"
