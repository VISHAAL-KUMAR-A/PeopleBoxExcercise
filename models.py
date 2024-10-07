from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
import json

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = ArrayField(models.CharField(max_length=100))
    experience_level = models.CharField(max_length=50)
    desired_roles = ArrayField(models.CharField(max_length=100))
    preferred_locations = ArrayField(models.CharField(max_length=100))
    job_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.username}'s profile"

class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    required_skills = ArrayField(models.CharField(max_length=100))
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50)
    experience_level = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.company}"
