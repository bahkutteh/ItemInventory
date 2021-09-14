from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from .forms import UserForm, RoleForm, ProductForm, ProductDetailForm, Order, OrderDetailForm, ReceiptForm
from main.models import User, Role, Product, Product_Detail, Order, Order_Detail, Receipt

#from .models import Product, Product_Detail

# Create your views here.

def user_list(request):
    queryset = User.objects.all()
    context = { 
        'qs': queryset
    }
    return render(request, "user_list.html", context)
    
def user_role(request):
    queryset = Role.objects.all()
    context = { 
        'qs': queryset
    }
    return render(request, "user_role.html", context)

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
	
#forms for each models

def Manage_User(request):
	UserForm = UserForm(Product, fields = ('username', 'user_email','user_password'))
	
	if request.method == 'POST':
		formset = UserFormSet(request.POST, request.FILES)
		if formset.is_valid():
			formset.save()
	else:
		formset = UserFormSet()
	return render (request, 'user_list.html', {'formset' : formset})
	
def Manage_User_Role(request):
	RoleForm = RoleForm(Product, fields = ('role_name', 'role_type'))

	if request.method == 'POST':
		formset = RoleFormSet(request.POST, request.FILES)
		if formset.is_valid():
			formset.save()
	else:
		formset = RoleFormSet()
	return render (request, 'user_role.html', {'formset' : formset})

def Manage_Product(request):
	ProductForm = ProductForm(Product, fields = ('product_name', 'product_type'))
	
	if request.method == 'POST':
		formset = ProductFormSet(request.POST, request.FILES)
		if formset.is_valid():
			formset.save()
	else:
		formset = ProductFormSet()
	return render (request, 'product_list.html', {'formset' : formset})

def Manage_Product_Detail(request):
	ProductDetailForm = ProductDetailForm(Product_Detail, fields = ('description','price'))
	
	if request.method == 'POST':
		formset = ProductDetailFormSet(request.POST, request.FILES)
		if formset.is_valid():
			formset.save()
	else:
		formset = UserFormSet()
	return render (request, 'product_detail.html', {'formset' : formset})
	
def Manage_Order(request):
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
	
def Manage_Receipt(request):
	ReceiptForm = ReceiptForm(Receipt, fields = ('barcode'))
	
	if request.method == 'POST':
		formset = ReceiptFormSet(request.POST, request.FILES)
		if formset.is_valid():
			formset.save()
	else:
		formset = ReceiptFormSet()
	return render (request, 'receipt.html', {'formset' : formset})