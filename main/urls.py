from django.urls import path
from .views import RegisterView, product_list

app_name = 'main'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('product/',product_list, name="product_list"),
]