from rest_framework.routers import DefaultRouter
from .views import PhoneViewSet, PhoneInfoViewSet, UserProfileViewSet, UserViewSet

router = DefaultRouter()
router.register('user', UserViewSet, basename='users')
router.register('phoneinfo', PhoneInfoViewSet)
router.register('userprofile',UserProfileViewSet)
router.register('', PhoneViewSet, basename='phones')


urlpatterns = router.urls