from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import UserProfile, Job
from .serializers import UserProfileSerializer, JobSerializer
from django.db.models import Q
from typing import List
import numpy as np

class JobRecommendationViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def calculate_job_match_score(self, user_profile: UserProfile, job: Job) -> float:
        score = 0.0
        
        # Skills match (40% weight)
        user_skills = set(user_profile.skills)
        job_skills = set(job.required_skills)
        skills_overlap = len(user_skills.intersection(job_skills))
        skills_score = skills_overlap / max(len(job_skills), 1) * 0.4
        score += skills_score
        
        # Experience level match (20% weight)
        if user_profile.experience_level == job.experience_level:
            score += 0.2
        
        # Location match (20% weight)
        if job.location in user_profile.preferred_locations:
            score += 0.2
        
        # Job type match (10% weight)
        if job.job_type == user_profile.job_type:
            score += 0.1
        
        # Desired role match (10% weight)
        if job.title in user_profile.desired_roles:
            score += 0.1
        
        return score

    @action(detail=False, methods=['GET'])
    def recommendations(self, request):
        try:
            user_profile = request.user.userprofile
        except UserProfile.DoesNotExist:
            return Response(
                {"error": "User profile not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )

        # Get all jobs
        jobs = Job.objects.all()

        # Calculate match scores
        job_scores = [
            (job, self.calculate_job_match_score(user_profile, job))
            for job in jobs
        ]

        # Sort by score and filter by minimum threshold
        recommended_jobs = [
            job for job, score in sorted(job_scores, key=lambda x: x[1], reverse=True)
            if score > 0.3
        ][:5]

        serializer = self.get_serializer(recommended_jobs, many=True)
        return Response(serializer.data)

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
