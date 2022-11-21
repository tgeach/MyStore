from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
from .models import Account, Inventory, Location, Order
# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

class InventoryAdmin(admin.ModelAdmin):
    list_display = ("name", "unit", "price_per_unit")

# Adds ability to import/export data from admin pannel 
class LocationResource(resources.ModelResource):
    account = Field(column_name="Account Name", attribute="account", widget=ForeignKeyWidget(Account, "name"))
    street_address = Field(attribute="street_address", column_name="Street Address")
    
    class Meta:
        model = Location
        skip_unchanged = True
        report_skipped = True
        feilds = (
            "id",
            "name",
            "accout",
            "street_address", 
            "city", 
            "province_state", 
            "country", 
            "zip_postal", 
            "contact_phone"
        )
        


class LocationAdmin(ImportExportModelAdmin):
    list_display = ("name", "account", "street_address", "city", "province_state", "country", "zip_postal", "contact_phone")

class OrderAdmin(admin.ModelAdmin):
    list_display = ("inventory", "account", "location", "user", "date", "quantity")

admin.site.register(Account, AccountAdmin)
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Order, OrderAdmin)