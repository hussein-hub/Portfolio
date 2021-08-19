from django.db import models
import django

# Create your models here.

class projects(models.Model):
    projectName = models.CharField(max_length=200)
    projectDescription = models.TextField(max_length=650)
    projectImage = models.ImageField(upload_to='projectInfo/')
    projectLink = models.URLField()


class feedback(models.Model):
    fullName = models.CharField(max_length=100)
    emailId = models.EmailField(max_length=150)
    phoneNumber = models.IntegerField()
    message = models.TextField(max_length=1000)
    messageDate = models.DateField(default=django.utils.timezone.now)
    subject = models.CharField(default="Improvements", max_length=250)