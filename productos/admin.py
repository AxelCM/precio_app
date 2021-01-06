from django.contrib import admin
from productos.models import *

from import_export import resources
from import_export.admin import ImportExportModelAdmin

"""MODEL RESOURCE"""
class ProductResource(resources.ModelResource):

    class Meta:
        model = Product
        import_id_fields = ('upc',)

class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['upc', 'name' , 'description' , 'price']
    resource_class = ProductResource

class PricerAdmin(admin.ModelAdmin):
    list_display = ['product_data' , 'cant']
    search_fields = ['product__name']
    resource_class = ProductResource

class ComputerResource(resources.ModelResource):

    class Meta:
        model = Computer
        import_id_fields = ('model',)

class ComputerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['model' , 'ofert_price' , 'normal_price']
    search_fields = ['computer__name']
    
    resource_class = ComputerResource



# Register your models here.
admin.site.register(TypeSize)
admin.site.register(Size)
admin.site.register(Season)
admin.site.register(Product, ProductAdmin)
admin.site.register(Pricer, PricerAdmin)
admin.site.register(Computer, ComputerAdmin)
admin.site.register(ComputerPricer)
# admin.site.register(Computer)
