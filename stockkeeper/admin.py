from django.contrib import admin
from mptt.admin import MPTTModelAdmin

# Register your models here.
from .models import(ComponentMeasurementUnit,
                    StorageArea,
                    StorageAreaType,
                    Component,
                    ComponentType,
                    ComponentPrice,
                    Currency,
                    Manufacturer,
                    Vendor)

class ComponentAdmin(admin.ModelAdmin):
    list_display = ("name", "component_type", "manufacturer", "vendor_display")

    def vendor_display(self, obj):
        try:
            return ", ".join([
                price.sell_at for price in obj.prices.all()
                ])
        except:
            return "No price available"

    vendor_display.short_description = "Prices"

class ComponentPriceAdmin(admin.ModelAdmin):
    list_display = ("vendor", "buy_at", "sell_at", "rrp")

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("name", "buy_direct", "reseller_discount_available")

class VendorAdmin(admin.ModelAdmin):
    list_display = ("name", "reseller_discount_available")

admin.site.register(ComponentMeasurementUnit)
admin.site.register(StorageArea, MPTTModelAdmin)
admin.site.register(StorageAreaType)
admin.site.register(Component, ComponentAdmin)
admin.site.register(ComponentType, MPTTModelAdmin)
admin.site.register(ComponentPrice, ComponentPriceAdmin)
admin.site.register(Currency)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Vendor, VendorAdmin)
