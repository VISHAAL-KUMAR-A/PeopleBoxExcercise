from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator, MaxValueValidator

class UserProfile(models.Model):
    EXPERIENCE_CHOICES = [
        ('Junior', 'Junior'),
        ('Intermediate', 'Intermediate'),
        ('Senior', 'Senior'),
    ]
    
    name = models.CharField(max_length=100)
    skills = ArrayField(models.CharField(max_length=50))
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserPreferences(models.Model):
    JOB_TYPE_CHOICES = [
        ('Full-Time', 'Full-Time'),
        ('Part-Time', 'Part-Time'),
        ('Contract', 'Contract'),
    ]
    
    user = models.OneToOneField(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='preferences'
    )
    desired_roles = ArrayField(models.CharField(max_length=100))
    locations = ArrayField(models.CharField(max_length=100))
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    min_salary = models.IntegerField(null=True, blank=True)
    remote_only = models.BooleanField(default=False)

class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ('Full-Time', 'Full-Time'),
        ('Part-Time', 'Part-Time'),
        ('Contract', 'Contract'),
    ]
    
    EXPERIENCE_CHOICES = [
        ('Junior', 'Junior'),
        ('Intermediate', 'Intermediate'),
        ('Senior', 'Senior'),
    ]
    
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    required_skills = ArrayField(models.CharField(max_length=50))
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES)
    description = models.TextField()
    salary_range_min = models.IntegerField(null=True, blank=True)
    salary_range_max = models.IntegerField(null=True, blank=True)
    is_remote = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
