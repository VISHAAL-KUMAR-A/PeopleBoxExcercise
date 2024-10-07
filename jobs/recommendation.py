from django.db.models import F, ExpressionWrapper, FloatField
from django.contrib.postgres.search import TrigramSimilarity
from .models import Job

class JobRecommender:
    def __init__(self, user_profile):
        self.user_profile = user_profile
        self.preferences = user_profile.preferences
    
    def calculate_skills_match(self, required_skills):
        user_skills = set(self.user_profile.skills)
        job_skills = set(required_skills)
        skills_overlap = len(user_skills.intersection(job_skills))
        return skills_overlap / max(len(job_skills), 1)
    
    def get_recommendations(self, limit=10):
        base_queryset = Job.objects.all()
        
        # Filter by job type if specified
        if self.preferences.job_type:
            base_queryset = base_queryset.filter(job_type=self.preferences.job_type)
        
        # Filter by location
        if self.preferences.locations:
            base_queryset = base_queryset.filter(location__in=self.preferences.locations)
        
        # Filter by remote preference
        if self.preferences.remote_only:
            base_queryset = base_queryset.filter(is_remote=True)
        
        # Calculate match scores
        scored_jobs = []
        for job in base_queryset:
            score = 0.0
            
            # Skills match (40%)
            skills_score = self.calculate_skills_match(job.required_skills) * 0.4
            
            # Experience level match (20%)
            experience_score = 0.2 if job.experience_level == self.user_profile.experience_level else 0
            
            # Location match (20%)
            location_score = 0.2 if job.location in self.preferences.locations else 0
            
            # Job type match (10%)
            job_type_score = 0.1 if job.job_type == self.preferences.job_type else 0
            
            # Desired role match (10%)
            role_score = 0.1 if job.title in self.preferences.desired_roles else 0
            
            total_score = skills_score + experience_score + location_score + job_type_score + role_score
            scored_jobs.append((job, total_score))
        
        # Sort by score and return top recommendations
        scored_jobs.sort(key=lambda x: x[1], reverse=True)
        return scored_jobs[:limit]
