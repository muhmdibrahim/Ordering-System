from django.urls import path
from .views import get_products, add_product, create_order, delete_product
urlpatterns = [
    path('', get_products, name='product_list'),
    path('add_product/', add_product, name='add_product'),
    path('create_order/', create_order, name='create_order'),
    path('delete_product/<int:product_id>/', delete_product, name='delete_product'),
]