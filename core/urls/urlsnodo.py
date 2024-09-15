from django.urls import path
from ..vistas.vistas_nodo import *
from ..vistas.vistas_detalles import *

urlpatterns = [
    path("", home, name="home"),
    path("lista", NodoList.as_view(), name="lista"), 
    path("detalle/<int:id_nodo>", DetalleNodos, name="detalle"), 
    path("borrar/<int:pk>", NodoBorrar.as_view(), name="borrar"), 
    path("editar/<int:pk>", NodoEditar.as_view(), name="editar"), 
    path("crear/", NodoCrear.as_view(), name="crear"), 
]


