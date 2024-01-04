from rest_framework import routers
from .views import PrinterViewSet, CheckViewSet

router = routers.DefaultRouter()
router.register(r'printers', PrinterViewSet)
router.register(r'checks', CheckViewSet)

urlpatterns = router.urls