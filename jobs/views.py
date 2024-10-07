from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import UserProfile, Job
from .serializers import UserProfileSerializer, JobSerializer
from .recommendation import JobRecommender

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    
    @action(detail=True, methods=['get'])
    def recommendations(self, request, pk=None):
        try:
            user_profile = self.get_object()
            recommender = JobRecommender(user_profile)
            recommendations = recommender.get_recommendations()
            
            # Prepare serialized response
            serialized_jobs = []
            for job, score in recommendations:
                job_data = JobSerializer(job).data
                job_data['match_score'] = round(score * 100, 2)
                serialized_jobs.append(job_data)
            
            return Response(serialized_jobs)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
