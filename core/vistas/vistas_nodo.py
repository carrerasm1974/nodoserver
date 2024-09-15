
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..modelos.modelsnodo import ClaseNodo
from ..modelos.modelsnodo import ClaseCBROperacion
from ..forms.formsNodos import NodoEditarForm, NodoCrearForm
from django.core.paginator import Paginator

def home(request):
    datos = {}
    return render(request, 'main.html',datos)


class NodoList(ListView):
    model = ClaseNodo
    template_name = "nodos/lista.html"
    def get_queryset(self, *args, **kwargs): #Override del metodo queryset para ordenar los resultados al revés
        qs = super(NodoList, self).get_queryset(*args, **kwargs) 
        qs = qs.order_by("grupo") 
        return qs

class NodoCrear(CreateView):
    model = ClaseNodo
    template_name = "nodos/crear.html"
    form_class = NodoCrearForm
    success_url = reverse_lazy("lista")

class NodoEditar(UpdateView):
    model = ClaseNodo
    template_name = "nodos/editar.html"
    form_class = NodoEditarForm
    success_url = reverse_lazy("lista")

class NodoBorrar(DeleteView):
    model = ClaseNodo
    template_name = "nodos/borrar.html"
    success_url = reverse_lazy('lista')

