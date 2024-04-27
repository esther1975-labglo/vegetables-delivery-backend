# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import OwnerProfile, DeliveryBoyProfile, UserProfile
from .serializers import OwnerProfileSerializer, DeliveryBoyProfileSerializer, UserProfileSerializer

class OwnerRegister(APIView):
    def post(self, request):
        serializer = OwnerProfileSerializer(data=request.data)
        if serializer.is_valid():
            user_data = serializer.validated_data['user']
            user = User.objects.create_user(username=user_data['username'], password=user_data['password'])
            user.email = user_data['email']
            user.save()
            owner_profile = OwnerProfile.objects.create(user=user, **serializer.validated_data)
            return Response({'message': 'Owner registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeliveryBoyRegister(APIView):
    def post(self, request):
        serializer = DeliveryBoyProfileSerializer(data=request.data)
        if serializer.is_valid():
            user_data = serializer.validated_data['user']
            user = User.objects.create_user(username=user_data['username'], password=user_data['password'])
            user.email = user_data['email']
            user.save()
            delivery_boy_profile = DeliveryBoyProfile.objects.create(user=user, **serializer.validated_data)
            return Response({'message': 'Delivery Boy registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRegister(APIView):
    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            user_data = serializer.validated_data['user']
            user = User.objects.create_user(username=user_data['username'], password=user_data['password'])
            user.email = user_data['email']
            user.save()
            user_profile = UserProfile.objects.create(user=user, **serializer.validated_data)
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

class UserLogout(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'Logged out successfully'})
