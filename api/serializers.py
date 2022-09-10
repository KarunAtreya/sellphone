from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Phone, PhoneInfo, UserProfile

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ('id','owner','brand','model','variant','storage','battery','touchorfaceid', 'truetone',
             'screen_issues', 'body_issues')
        

class PhoneInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneInfo
        fields = ('phone', 'description', 'image', 'color', 'price', 'negotiable')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username','email')

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user', 'phone_number', 'location', 'profile_pic',)

       