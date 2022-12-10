from django.urls import path
from .  import views

app_name = "producto_app"

urlpatterns = [
    path('add_product/', views.ProductoCreateView.as_view(), name="product_add"),
    path('list_product/', views.ProductoListView.as_view(), name="product_list"),
    path('update_product/<pk>/', views.ProductoUpdateView.as_view(), name="product_update"),


]
