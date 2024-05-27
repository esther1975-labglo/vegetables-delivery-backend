# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    OrderViewSet,
    OwnerViewSet, 
    DeliveryBoyViewSet, 
    UserProfileViewSet, 
    UserLogin, 
    UserLogout,
    ProductViewSet
)

router = DefaultRouter()
router.register(r'user', UserProfileViewSet)
router.register(r'delivery-boy', DeliveryBoyViewSet)
router.register(r'owner', OwnerViewSet)
router.register(r'product', ProductViewSet)
router.register(r'order', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
]
