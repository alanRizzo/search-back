from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Item, Categoria


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'codigo',
        'nombre',
        'categoria',
        'precio',
    )


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', )


admin.site.unregister(Group)
