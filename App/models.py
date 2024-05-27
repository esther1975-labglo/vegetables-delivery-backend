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

class Product(models.Model):
    CATEGORY_CHOICES = (
        ("Vegetable", "Vegetable"),
        ("Fruit", "Fruit"),
        ("Nut", "Nut"),
        ("Dal", "Dal"),
        ("Meat", "Meat")
    )
    owner = models.ForeignKey(OwnerProfile, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="Products")

    def __str__(self):
        return self.name
    

class Order(models.Model):
    STATUS_CHOICES = (
        ("ordered", "Ordered"),
        ("shipped", "Shipped"),
        ("delivered", "Delivered")
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    delivery_boy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='deliveries')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="ordered")
    address = models.TextField()