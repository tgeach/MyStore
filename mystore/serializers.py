from rest_framework import serializers
from .models import Account, Inventory, Location, Order



class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["id", "name", "user"]

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = "__all__"

class LocationSerializer(serializers.ModelSerializer):
    #displays the account as a nested object
    #account = AccountSerializer(read_only=True)
    # the account name will display rather than the id
    account = serializers.CharField(source="account.name")

    class Meta:
        model = Location
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    # account = serializers.IntegerField(read_only=True)
    # quantity = serializers.IntegerField(read_only=True)
    # inventory = serializers.CharField(read_only=True)
    # location = serializers.IntegerField(read_only=True)
    # day = serializers.DateField(read_only=True)
    account_name = serializers.CharField(read_only=True, source='account.name')
    inventory_name = serializers.CharField(read_only=True, source='inventory.name')
    location_name = serializers.CharField(read_only=True, source='location.name')
    

    class Meta:
        model = Order
        fields = (
            "account_name",
            "location_name",
            "inventory_name",
            "quantity",         

        )