from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, ClienteViewSet, VentaViewSet, CategoriaList, total_ventas

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'ventas', VentaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('categorias/', CategoriaList.as_view(), name='categorias'),
    path('total-ventas/', total_ventas, name='total_ventas'),
]
