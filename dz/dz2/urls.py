from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('order/', views.order_list, name='order_list'),
    path('order/order_cart/', views.order_cart, name='order_cart'),
    path('order/create/', views.order_create, name='order_create'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('order/<int:order_id>/update/', views.order_update, name='order_update'),
    path('order/<int:order_id>/delete/', views.order_delete, name='order_delete'),

    path('client/', views.client_list, name='client_list'),
    path('client/create/', views.create_client, name='client_create'),
    path('client/<int:client_id>/', views.client_detail, name='client_detail'),
    path('client/<int:client_id>/update/', views.update_client, name='client_update'),
    path('client/<int:client_id>/delete/', views.delete_client, name='client_delete'),

    path('product/', views.product_list, name='product_list'),
    path('product/create/', views.product_detail, name='product_create'),
    path('product/<int:product_id>/', views.product_view, name='product_view'),
    path('product/<int:product_id>/update/', views.update_product, name='product_update'),
    path('product/<int:product_id>/delete/', views.delete_product, name='product_delete'),
]