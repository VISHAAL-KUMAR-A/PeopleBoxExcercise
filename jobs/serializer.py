from rest_framework import serializers
from .models import UserProfile, UserPreferences, Job

class UserPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPreferences
        exclude = ('user',)

class UserProfileSerializer(serializers.ModelSerializer):
    preferences = UserPreferencesSerializer()
    
    class Meta:
        model = UserProfile
        fields = '__all__'
    
    def create(self, validated_data):
        preferences_data = validated_data.pop('preferences')
        user_profile = UserProfile.objects.create(**validated_data)
        UserPreferences.objects.create(user=user_profile, **preferences_data)
        return user_profile

class JobSerializer(serializers.ModelSerializer):
    match_score = serializers.FloatField(read_only=True, required=False)
    
    class Meta:
        model = Job
        fields = '__all__'
