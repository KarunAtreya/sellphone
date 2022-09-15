from rest_framework.routers import DefaultRouter
from .views import PhoneViewSet, UserProfileViewSet, UserViewSet

router = DefaultRouter()
router.register('user', UserViewSet, basename='users')
router.register('userprofile',UserProfileViewSet)
router.register('phone', PhoneViewSet, basename='phones')

urlpatterns = router.urls