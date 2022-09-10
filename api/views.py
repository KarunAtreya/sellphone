from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .permissions import IsAuthorOrReadOnly, IsAuthorOrReadOnly1, IsAuthorOrReadOnly2, IsUserOrReadOnly
from .models import Phone, PhoneInfo, UserProfile
from .serializers import PhoneInfoSerializer, PhoneSerializer, UserProfileSerializer, UserSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class PhoneViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly)
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

class PhoneInfoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly1, IsAuthenticatedOrReadOnly)
    parser_classes =[MultiPartParser, FormParser]
    queryset = PhoneInfo.objects.all()
    serializer_class = PhoneInfoSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsUserOrReadOnly,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly2, IsAuthenticatedOrReadOnly)
    parser_classes =[MultiPartParser, FormParser]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
