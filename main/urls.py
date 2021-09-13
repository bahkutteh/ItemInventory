from django.urls import path
from .views import RegisterView, product_list, product_detail, order_list, order_detail

app_name = 'main'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('product/',product_list, name="product_list"),
    path('product/detail',product_detail, name="product_detail"),
    path('order/',order_list, name="order_list"),
    path('order/detail',order_detail, name="order_detail"),
    
]