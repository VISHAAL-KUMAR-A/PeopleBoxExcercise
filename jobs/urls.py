from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobRecommendationViewSet, UserProfileViewSet

router = DefaultRouter()
router.register(r'jobs', JobRecommendationViewSet)
router.register(r'profiles', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
