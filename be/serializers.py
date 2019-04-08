from rest_framework import serializers
from .models import Item, Categoria


class ItemSerializer(serializers.ModelSerializer):
    categoria_nombre = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = ('id', 'codigo', 'nombre', 'categoria', 'categoria_nombre', 'precio', 'stock')

    def get_categoria_nombre(self, obj):
        return obj.categoria.nombre


class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = ('id', 'nombre')
