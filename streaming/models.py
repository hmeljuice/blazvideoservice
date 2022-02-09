from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Video(models.Model):
    """Model for videos info"""
    title = models.CharField(max_length=200)

    description = models.TextField(max_length=500, help_text="Enter short description")

    file_location = models.FileField()

    lender = models.ManyToManyField(User, null=True, blank=True)

    class Meta:
        ordering = ['title']


    def __str__(self):
        """String for representing Videos model"""
        return f'{self.title}'


