from django.db import models
from django.core.validators import MinValueValidator
from django_prometheus.models import ExportModelOperationsMixin

# Create your models here.
class StorageAreaType(ExportModelOperationsMixin('StorageAreaType'), models.Model):
    type_name = models.CharField(max_length=10)
    type_description = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.type_name

class StorageArea(ExportModelOperationsMixin('StorageArea'), models.Model):
    storage_area_name = models.CharField(max_length=100)
    storage_area_type = models.ForeignKey(StorageAreaType, on_delete=models.CASCADE)
    parent_area = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.storage_area_name

class ComponentMeasurementUnit(ExportModelOperationsMixin('ComponentMeasurementUnit'), models.Model):
    unit_name = models.CharField(max_length=10)
    unit_description = models.CharField(max_length=200,null=True, blank=True)

    def __str__(self):
        return self.unit_name

class ComponentType(ExportModelOperationsMixin('ComponentType'), models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Component(ExportModelOperationsMixin('Component'), models.Model):
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=100)
    mpn = models.CharField(max_length=100, null=True, blank=True)
    upc = models.IntegerField(null=True, blank=True)
    component_type = models.ForeignKey(ComponentType, on_delete=models.CASCADE)
    storage_area = models.ManyToManyField(StorageArea)
    measurement_unit = models.ForeignKey(ComponentMeasurementUnit, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name


