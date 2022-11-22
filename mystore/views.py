from django.shortcuts import render
from .models import Account, Inventory, Location, Order
from .serializers import AccountSerializer, InventorySerializer, LocationSerializer, OrderSerializer
from rest_framework import viewsets
from django.db.models import Sum
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


class OrderViewSet(viewsets.ModelViewSet):
    # queryset = Order.objects.annotate(day=TruncDay("date")).values("day")
    queryset=Order.objects.all()
    serializer_class = OrderSerializer