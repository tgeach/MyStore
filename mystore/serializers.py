from rest_framework import serializers
from .models import Account, Inventory, Location, Order



class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["id", "name", "user"]

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = (
            "id",
            "name",
            "unit",
            "price_per_unit"
        )

class LocationSerializer(serializers.ModelSerializer):
    #displays the account as a nested object
    #account = AccountSerializer(read_only=True)
    # the account name will display rather than the id
    account = serializers.CharField(source="account.name")

    class Meta:
        model = Location
        fields = "__all__"

class OrderFieldSerializer(serializers.ModelSerializer):
    account = serializers.CharField(read_only=True)
    location = serializers.CharField(read_only=True)
    inventory = serializers.CharField(read_only=True)
    quantity = serializers.IntegerField(read_only=True)
    price_per_unit = serializers.DecimalField(read_only=True, max_digits=5, decimal_places=2, source="inventory.price_per_unit")

    class Meta: 
        model = Order
        fields = (
            "account",
            "location",
            "inventory",
            "price_per_unit",
            "quantity",
        )

class OrderLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "date",
            "order"
        )

    order = serializers.SerializerMethodField('get_order')

    def get_order(self, obj):
        orders = Order.objects.filter(date=obj['date'])
        order_serializer = OrderFieldSerializer(orders, many=True)
        return order_serializer.data

