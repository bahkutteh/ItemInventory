from django.contrib import admin
from .models import Product, Product_Detail, Order, Order_Detail

# Register your models here.

admin.site.register(Product)
admin.site.register(Product_Detail)
admin.site.register(Order)
admin.site.register(Order_Detail)