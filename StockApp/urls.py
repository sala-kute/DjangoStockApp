from django.urls import path
from .views import product_list , sales_list ,add_sale , error, stock_list,purchase_list,add_purchase,dashboard 

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('sales/', sales_list, name='sales_list'),
    path('purchases/', purchase_list, name='purchase_list'),
    path('add_sale/', add_sale, name='add_sale'),
    path('add_purchase/', add_purchase, name='add_purchase'),
    path('stocks/', stock_list, name='stock_list'),
    path('dashboard/', dashboard, name='dashboard'),
    path('error/', error, name='error'),



    # Add other URL patterns for purchase, sale, supplier, customer, and stock as needed
]