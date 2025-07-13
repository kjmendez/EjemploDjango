from django.shortcuts import render

from rest_framework import viewsets, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Producto, Cliente, Categoria, Venta
from .serializers import ProductoSerializer, ClienteSerializer, CategoriaSerializer, VentaSerializer
from django.http import HttpResponse

# ModelViewSets
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    permission_classes = [IsAuthenticated]

# GenericAPIView
class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]

# Custom API
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def total_ventas(request):
    total = Venta.objects.count()
    return Response({"total_ventas": total})
def home(request):
    return HttpResponse("Bienvenido al sistema de ventas")
