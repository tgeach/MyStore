from django.contrib import admin
from .models import Account, Inventory, Location, Order
# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

class InventoryAdmin(admin.ModelAdmin):
    list_display = ("name", "unit", "price_per_unit")

class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "account", "street_address", "city", "province_state", "country", "zip_postal", "contact_phone")

class OrderAdmin(admin.ModelAdmin):
    list_display = ("inventory", "account", "location", "user", "date", "quantity")

admin.site.register(Account, AccountAdmin)
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Order, OrderAdmin)