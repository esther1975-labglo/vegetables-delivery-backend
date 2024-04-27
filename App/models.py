# models.py
from django.contrib.auth.models import User
from django.db import models


class OwnerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='owner_profile')
    business_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=20)

class DeliveryBoyProfile(models.Model):
    GENDER_CHOICES = (
        ("male", "male"),
        ("female", "female")
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='delivery_boy_profile')
    vehicle_type = models.CharField(max_length=50)
    vehicle_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_joining = models.DateField() 
    availability = models.BooleanField(default=True)
    address = models.TextField()

class UserProfile(models.Model):
    GENDER_CHOICES = (
        ("male", "male"),
        ("female", "female")
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address = models.TextField()