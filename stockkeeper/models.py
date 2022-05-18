from django.db import models
from django.core.validators import MinValueValidator
from django_prometheus.models import ExportModelOperationsMixin

from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class StorageAreaType(ExportModelOperationsMixin('StorageAreaType'), models.Model):
    type_name = models.CharField(max_length=10)
    type_description = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.type_name

class StorageArea(ExportModelOperationsMixin('StorageArea'), MPTTModel):
    name = models.CharField(max_length=100)
    storage_area_type = models.ForeignKey(StorageAreaType, on_delete=models.CASCADE)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

class ComponentMeasurementUnit(ExportModelOperationsMixin('ComponentMeasurementUnit'), models.Model):
    unit_name = models.CharField(max_length=10)
    unit_description = models.CharField(max_length=200,null=True, blank=True)

    def __str__(self):
        return self.unit_name

class ComponentType(ExportModelOperationsMixin('ComponentType'), MPTTModel):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    shortcode = models.CharField(max_length=3)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

class Manufacturer(ExportModelOperationsMixin('Manufacturer'), models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField()
    primary_contact_email = models.EmailField()
    buy_direct = models.BooleanField()
    reseller_discount_available = models.BooleanField()
    
    def __str__(self):
        return self.name

class Vendor(ExportModelOperationsMixin('Vendor'), models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField()
    primary_contact_email = models.EmailField()
    reseller_discount_available = models.BooleanField()
    
    def __str__(self):
        return self.name

class Currency(ExportModelOperationsMixin('Currency'), models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=3)
    symbol = models.CharField(max_length=2)

    class Meta:
        verbose_name_plural = "currencies"

    def __str__(self):
        return self.symbol

class ComponentPrice(ExportModelOperationsMixin('Vendor'), models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    rrp = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    buy_at = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    sell_at = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    buy_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='buy_currency')
    sell_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='sell_currency')

    def __str__(self):
        return f"{self.vendor} - {self.sell_currency}{self.sell_at}"

class Component(ExportModelOperationsMixin('Component'), models.Model):
    name = models.CharField(max_length=200)
    mpn = models.CharField(max_length=100, null=True, blank=True)
    upc = models.IntegerField(null=True, blank=True)
    prices = models.ForeignKey(ComponentPrice, on_delete=models.CASCADE, null=True, blank=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True, blank=True)
    component_type = models.ForeignKey(ComponentType, on_delete=models.CASCADE)
    storage_area = models.ManyToManyField(StorageArea)
    measurement_unit = models.ForeignKey(ComponentMeasurementUnit, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name


