from django.contrib import admin
from .models import Category, Product, Order, OrderItem

# Register your models here.

@admin.register(Category)
class TodoList(admin.ModelAdmin):
    list_display = (
        "name",
    )

@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = (
        "category",
        "name",
        "price",
        "description",
        "image",
    )

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = (
        "user",
        "total_price",
        "ordered_date",
        "is_ordered",
    )
    inlines = [OrderItemInline,]
