from django.shortcuts import render
from .models import Account, Inventory, Location, Order
from .serializers import AccountSerializer, InventorySerializer, LocationSerializer, OrderFieldSerializer, OrderLogSerializer
from rest_framework import viewsets
from django.db.models import Count, Sum
from django.db.models.functions import TruncDate, TruncDay


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class OrderFieldViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderFieldSerializer

class OrderLogViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.order_by('date').values('date').distinct()
    serializer_class = OrderLogSerializer