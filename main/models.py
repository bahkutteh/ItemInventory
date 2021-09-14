from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.


class Role(models.Model):
	role_name = models.TextField(blank=True)
	class Role_Type (models.IntegerChoices):
		admin = 1
		staff = 2
		customer = 3
		
	role_type = models.IntegerField(choices=Role_Type.choices)
	
	def __str__(self):
		return self.role_name
	
class User(models.Model):
	role = models.ForeignKey(Role, on_delete=models.CASCADE, blank=False)
	username = models.TextField(blank=True)
	user_email = models.EmailField(max_length=250, blank=True)
	user_password = models.TextField(blank=True)
	
	def __str__(self):
		return self.username
	
class Product(models.Model):
	product_name = models.CharField(max_length=50, blank=True)
	product_type = models.CharField(max_length=50, blank=True)
	
	
	def __str__(self):
		return self.product_name
		
	

class Product_Detail(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False)
	description = models.TextField(blank=True)
	price = models.FloatField(blank=True)
	
	
	def __str__(self):
		return self.description

class Order(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False)
	quantity = models.IntegerField(blank=True)
	
	def __str__(self):
		return self.quantity

class Order_Detail(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
	order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=False)
	shipping_address = models.TextField(blank=True)
	total_price = models.FloatField(blank=True)
	date = models.DateTimeField(default=timezone.now, blank=True)
	
	def __str__(self):
		return self.shipping_address

class Receipt(models.Model):
	order_detail = models.ForeignKey(Order_Detail, on_delete=models.CASCADE, blank=False)
	barcode = models.BinaryField(max_length=150, blank=True)
	
	def __str__(self):
		return self.barcode