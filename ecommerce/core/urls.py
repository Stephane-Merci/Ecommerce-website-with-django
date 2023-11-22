from django.urls import path
from . import views

urlpatterns = [
    
    #home and shop
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),

    #category
    path('category/', views.category, name='category'),
    path('category_products/<cid>', views.category_products_list_view, name='category_products_list'),
    
    #vendor
    path('vendors/', views.vendor, name='vendor'),
]
