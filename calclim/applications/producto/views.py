from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView

#modelos
from .models import Producto

#formularios
from .forms import ProductoForm


# Create your views here.

class ProductoCreateView(CreateView):
    template_name = 'producto/add_producto.html'
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy('producto_app:product_list')

class ProductoListView(ListView):
    template_name = 'producto/list_producto.html'
    model = Producto
    context_object_name = 'productos'

class ProductoUpdateView(UpdateView):
    template_name = "producto/update_producto.html"
    model = Producto
    fields = (
        'nombre',
        'categoria',
        'precio',
        'cantidad',
        'estado',
    )

    success_url = reverse_lazy('producto_app:product_list')