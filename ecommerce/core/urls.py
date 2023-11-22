from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('category/', views.category, name='category'),
    path('category_products/<cid>', views.category_products_list_view, name='category_products_list'),

]
