from django.urls import path
from .views import RegisterView, product_list, product_detail, order_list, order_detail
from . import views

app_name = 'main'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    
    path('product/', views.product_list, name="product_list"),
    path('product/detail/',product_detail, name="product_detail"),
    
    path ('create_product/', views.CreateProduct, name="create_product"),
    path('update_product/<str:pk>/', views.updateProduct, name= "update_product"),
    path('delete_product/<str:pk>/', views.deleteProduct, name= "delete_product"),
    path('create_product/detail/', views.CreateProductDetail, name= "create_product_detail"),
    
    path('order/',order_list, name="order_list"),
    path('order/detail/',order_detail, name="order_detail"),
    
    path('create_order/', views.CreateOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name= "update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name= "delete_order"),
    path('create_order/detail/', views.CreateOrderDetail, name= "create_order_detail"),
     
]