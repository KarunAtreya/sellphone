from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Phone, UserProfile

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ('id','owner','brand','model','storage','color','battery','screen_size', 'camera',
             'description', 'price', 'negotiable', 'image1', 'image2', 'image3', 'image4')
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username','email')

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user', 'phone_number', 'location', 'profile_pic',)

       