from django.urls import path, include
import mystore.views
from rest_framework import routers


router=routers.DefaultRouter()
router.register(r"accounts", mystore.views.AccountViewSet)
router.register(r"inventory", mystore.views.InventoryViewSet)
router.register(r"locations", mystore.views.LocationViewSet)
router.register(r"orders", mystore.views.OrderViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

