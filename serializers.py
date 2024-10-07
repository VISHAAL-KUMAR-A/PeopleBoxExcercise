from rest_framework import serializers
from .models import UserProfile, Job
from django.contrib.auth.models import User

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['skills', 'experience_level', 'desired_roles', 
                 'preferred_locations', 'job_type']

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
