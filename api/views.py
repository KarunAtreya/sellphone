from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .permissions import IsAuthorOrReadOnly, IsUserOrReadOnly1, IsUserOrReadOnly
from .models import Phone,  UserProfile
from .serializers import PhoneSerializer, UserProfileSerializer, UserSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class PhoneViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly)
    parser_classes =[MultiPartParser, FormParser]
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsUserOrReadOnly,IsAuthenticatedOrReadOnly)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (IsUserOrReadOnly1, IsAuthenticatedOrReadOnly)
    parser_classes =[MultiPartParser, FormParser]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
