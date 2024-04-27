# serializers.py
from rest_framework import serializers
from .models import UserProfile, OwnerProfile, DeliveryBoyProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class OwnerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnerProfile
        fields = '__all__'

class DeliveryBoyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryBoyProfile
        fields = '__all__'
