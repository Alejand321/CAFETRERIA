from django.contrib import admin
from . import models

class ProductoAdmin(admin.ModelAdmin):
    list_display =["nombre", "precio"]
    list_editable =["precio"]
    search_fields =["nombre"]
    
admin.site.register(models.Producto, ProductoAdmin)
