from django.urls import path, include
from mystore import views
from rest_framework import routers


router=routers.DefaultRouter()
router.register(r"accounts", views.AccountViewSet)
router.register(r"inventory", views.InventoryViewSet)
router.register(r"locations", views.LocationViewSet)
router.register(r"order_log", views.OrderLogViewSet, basename='order logs')
router.register(r"order_fields", views.OrderFieldViewSet, basename="order fields")


urlpatterns = [
    path("", include(router.urls)),
    
]

