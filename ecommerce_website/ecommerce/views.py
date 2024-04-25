from django.shortcuts import render
from.models import Category, Product, Order, OrderItem

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request, 'ecommerce/product_list.html', {'products': products})
