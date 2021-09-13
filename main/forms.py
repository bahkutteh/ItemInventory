from django.forms import ModelForm
from main.models import Product, Product_Detail,Order, Order_Detail

#create the form class.

#class UserForm(ModelForm):
#	class Meta:
#		model= User
#		fields: ['username','user_email','user_password']
		
#class RoleForm(ModelForm):
#	class Meta:
#		model= Role
#		fields: ['role_name','role_type']

class ProductForm(ModelForm):
	class Meta:
		model= Product
		fields = ['product_name', 'product_type']
		
class ProductDetailForm(ModelForm):
	class Meta:
		models= Product_Detail
		fields = ['description','price']
		
class OrderForm(ModelForm):
	class Meta:
		model= Order
		fields = ['quantity']

class OrderDetailForm(ModelForm):
	class Meta:
		model= Order_Detail
		fields = ['shipping_address', 'total_price','date']
		
#class ReceiptForm(ModelForm):
#	class Meta:
#		model= Receipt
#		fields = ['barcode']
		