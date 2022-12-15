from django.shortcuts import render
from .models import Account, Inventory, Location, Order
from .serializers import AccountSerializer, InventorySerializer, LocationSerializer, OrderFieldSerializer, OrderLogSerializer
from rest_framework import filters, viewsets
from django.db.models import Count, Sum
from django.db.models.functions import TruncDate, TruncDay
from rest_framework.permissions import IsAuthenticated


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
    permission_classes = [IsAuthenticated]
    serializer_class = OrderFieldSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^inventory__name']

    def get_queryset(self):

        #filters orders so that only the logged in user can see orders they've made
        user = self.request.user
        return Order.objects.filter(user=user)

class OrderLogViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.order_by('date').values('date').distinct()
    serializer_class = OrderLogSerializer
    