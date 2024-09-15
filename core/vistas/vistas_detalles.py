
from django.shortcuts import render
from ..modelos.modelsnodo import ClaseCBROperacion, ClaseNodo
from django.core.paginator import Paginator

def DetalleNodos(request, id_nodo):
    context = {}
    context['nodo'] = ClaseNodo.objects.get(pk=id_nodo)
    context['operaciones'] = ClaseCBROperacion.objects.filter(id_nodo=id_nodo)
    paginator = Paginator(context['operaciones'], 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    context['page_obj'] = paginator.get_page(page_obj)
    return render(request, 'nodos/detalle.html',context)
