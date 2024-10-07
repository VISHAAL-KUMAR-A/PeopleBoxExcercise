from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, JobViewSet

router = DefaultRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'jobs', JobViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
