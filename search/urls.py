from rest_framework.routers import DefaultRouter

from .views import PhoneDocumentView

router = DefaultRouter()
router.register(r'phone', PhoneDocumentView, basename='phonedocument')

urlpatterns = router.urls