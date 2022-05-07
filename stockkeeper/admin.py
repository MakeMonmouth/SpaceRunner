from django.contrib import admin

# Register your models here.
from .models import(ComponentMeasurementUnit,
                    StorageArea,
                    StorageAreaType,
                    Component,
                    ComponentType)

admin.site.register(ComponentMeasurementUnit)
admin.site.register(StorageArea)
admin.site.register(StorageAreaType)
admin.site.register(Component)
admin.site.register(ComponentType)
