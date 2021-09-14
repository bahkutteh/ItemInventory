from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from .forms import ProductForm, ProductDetailForm, OrderForm, OrderDetailForm
from main.models import Product, Product_Detail, Order, Order_Detail

#from .models import Product, Product_Detail

# Create your views here.

#def user_list(request):
#    queryset = User.objects.all()
#    context = { 
#        'qs': queryset
#    }
#    return render(request, "user_list.html", context)
    
#def user_role(request):
#    queryset = Role.objects.all()
#    context = { 
#        'qs': queryset
#    }
#   return render(request, "user_role.html", context)

def product_list(request):
    queryset = Product.objects.all()
    context = { 
        'qs': queryset
    }
    return render(request, "product_list.html", context)

def product_detail(request):
    queryset = Product_Detail.objects.all()
    context = { 
        'qs': queryset
    }
    return render(request, "product_detail.html", context)
    
def order_list(request):
    queryset = Order.objects.all()
    context = { 
        'qs': queryset
    }
    return render(request, "order_list.html", context)
    
def order_detail(request):
    queryset = Order_Detail.objects.all()
    context = { 
        'qs': queryset
    }
    return render(request, "order_detail.html", context)

def receipt(request):
    queryset = Receipt.objects.all()
    context = { 
        'qs': queryset
    }
    return render(request, "receipt.html", context)
	
class RegisterView(generic.CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'registration/register.html'
	

def CreateOrder(request):	#creating an order (update)
	
	form=OrderForm()
	if request.method == 'POST':
		form = OrderForm (request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
			
	context ={'form':form}
	
	return render (request, 'creating/order_form.html',context)
	
def updateOrder(request, pk):	#updating order
	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)
	context = {'form':form}
	return render (request, 'creating/order_form.html', context)
	
	if request.method == 'POST':
		form = OrderForm (request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')
			
def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == 'POST':
		order.delete()
		return redirect ('/')
	
	context = {{'item':order}}
	return render(request, 'account/delete.html', context)

def CreateOrderDetail(request):	#adding an Order detail (update)
	
	form=OrderDetailForm()
	if request.method == 'POST':
		form = OrderDetailForm (request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
			
	context ={'form':form}
	
	return render (request, 'creating/order_info_form.html',context)
	
def CreateProduct(request):	#creating an product
	
	form=ProductForm()
	if request.method == 'POST':
		form = ProductForm (request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
			
	context ={'form':form}
	
	return render (request, 'creating/product_form.html',context)

def updateProduct(request, pk):		#updating product
	order = Product.objects.get(id=pk)
	form = ProductForm(instance=order)
	context = {'form':form}
	return render (request, 'creating/product_form.html', context)
	
	if request.method == 'POST':
		form = ProductForm (request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')
			
def deleteProduct(request, pk):		#delete product
	product = Product.objects.get(id=pk)
	if request.method == 'POST':
		product.delete()
		return redirect ('/')
	
	context = {{'item':product}}
	return render(request, 'account/delete.html', context)

def CreateProductDetail(request):	#adding an Product detail 
	
	form=ProductDetailForm()
	if request.method == 'POST':
		form = ProductDetailForm (request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
			
	context ={'form':form}
	
	return render (request, 'creating/product_info_form.html',context)




#forms for each models

#def Manage_User(request):
#	UserForm = UserForm(Product, fields = ('username', 'user_email','user_password'))
	
#	if request.method == 'POST':
#		formset = UserFormSet(request.POST, request.FILES)
#		if formset.is_valid():
#			formset.save()
#	else:
#		formset = UserFormSet()
#	return render (request, 'user_list.html', {'formset' : formset})
	
#def Manage_User_Role(request):
#	RoleForm = RoleForm(Product, fields = ('role_name', 'role_type'))
#
#	if request.method == 'POST':
#		formset = RoleFormSet(request.POST, request.FILES)
#		if formset.is_valid():
#			formset.save()
#	else:
#		formset = RoleFormSet()
#	return render (request, 'user_role.html', {'formset' : formset})

def Manage_Product(request):	#show product
	ProductForm = ProductForm(Product, fields = ('product_name', 'product_type'))
	
	if request.method == 'POST':
		formset = ProductFormSet(request.POST, request.FILES)
		if formset.is_valid():
			formset.save()
	else:
		formset = ProductFormSet()
	return render (request, 'product_list.html', {'formset' : formset})

def Manage_Product_Detail(request):	#show product detail
	ProductDetailForm = ProductDetailForm(Product_Detail, fields = ('description','price'))
	
	if request.method == 'POST':
		formset = ProductDetailFormSet(request.POST, request.FILES)
		if formset.is_valid():
			formset.save()
	else:
		formset = UserFormSet()
	return render (request, 'product_detail.html', {'formset' : formset})
	
def Manage_Order(request):	#show order
	OrderForm = OrderForm(Order, fields = ('quantity'))
	
	if request.method == 'POST':
		formset = OrderFormSet(request.POST, request.FILES)
		if formset.is_valid():
			formset.save()
	else:
		formset = OrderFormSet()
	return render (request, 'order_list.html', {'formset' : formset})
	
def Manage_Order_Detail(request):
	OrderDetailForm = OrderDetailForm(Order_Detail, fields = ('shipping_address', 'total_price','date'))
	
	if request.method == 'POST':
		formset = OrderDetailFormSet(request.POST, request.FILES)
		if formset.is_valid():
			formset.save()
	else:
		formset = OrderDetailFormSet()
	return render (request, 'order_detail.html', {'formset' : formset})
	
#def Manage_Receipt(request):
#	ReceiptForm = ReceiptForm(Receipt, fields = ('barcode'))
#	
#	if request.method == 'POST':
#		formset = ReceiptFormSet(request.POST, request.FILES)
#		if formset.is_valid():
#			formset.save()
#	else:
#		formset = ReceiptFormSet()
#	return render (request, 'receipt.html', {'formset' : formset})