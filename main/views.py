from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render

from .models import Product

# Create your views here.

def product_list(request):
    queryset = Product.objects.all()
    context = { 
        'qs': queryset
    }
    return render(request, "product_list.html", context)


class RegisterView(generic.CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'registration/register.html'