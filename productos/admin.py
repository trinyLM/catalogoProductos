from django.contrib import admin
from .models import Categoria,Producto
# Register your models here.

#custom fields in admin
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre',"marca",'precio',)
    search_fields=["nombre",'marca',]
    list_filter = ('nombre',"marca",'precio',)
  

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields=['nombre']
    list_filter = ("nombre",)
  


admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Producto,ProductoAdmin)





#custom admin 

admin.site.site_header = "Global Paper Machinery"
admin.site.site_title = "Administracion del Catalogo"