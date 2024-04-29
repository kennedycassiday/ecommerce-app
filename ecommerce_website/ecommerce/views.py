from django.shortcuts import render, get_object_or_404, redirect
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

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    order, created = Order.objects.get_or_create(user=request.user, is_ordered=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
    order_item.quantity += 1
    order_item.save()
    return redirect('product_list')
