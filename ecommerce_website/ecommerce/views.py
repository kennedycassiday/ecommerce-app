from django.shortcuts import render, get_object_or_404
from.models import Category, Product, Order, OrderItem

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'ecommerce/product_list.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product_detail': product,
    }
    return render(request, 'ecommerce/product_detail.html', context)
