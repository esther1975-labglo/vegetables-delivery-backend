# urls.py
from django.urls import path
from .views import OwnerRegister, DeliveryBoyRegister, UserRegister, UserLogin, UserLogout

urlpatterns = [
    path('owner/register/', OwnerRegister.as_view(), name='owner-register'),
    path('delivery-boy/register/', DeliveryBoyRegister.as_view(), name='delivery-boy-register'),
    path('user/register/', UserRegister.as_view(), name='user-register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
]
