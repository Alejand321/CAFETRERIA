from rest_framework import viewsets 
from .models import Producto
from .serializers import ProductoSerializer

class ProductosViewSet(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    queryset =Producto.objects.all()