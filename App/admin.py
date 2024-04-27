from django.contrib import admin
from .models import UserProfile, DeliveryBoyProfile, OwnerProfile

admin.site.register(UserProfile)
admin.site.register(DeliveryBoyProfile)
admin.site.register(OwnerProfile)