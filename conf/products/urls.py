from django.urls import path
from .views import products_list, add_new_product

urlpatterns = [
    path('', products_list, name='products_list'),
    path('add', add_new_product, name='add_new_product'),
]
